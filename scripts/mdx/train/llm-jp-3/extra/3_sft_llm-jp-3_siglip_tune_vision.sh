#!/bin/bash

#SBATCH --job-name=0051_vila_extra       # name
#SBATCH --nodes=4                        # nodes
#SBATCH --ntasks-per-node=1              # crucial - only 1 task per dist per node!
#SBATCH --gres=gpu:8                     # number of gpus
#SBATCH --time 96:00:00                  # maximum execution time (HH:MM:SS)
#SBATCH --output=step_2_20241006.out     # output file name
#SBATCH --error=step_2_20241006.err
#SBATCH --partition=gpu

export GPUS_PER_NODE=8
export MASTER_ADDR=$(scontrol show hostnames $SLURM_JOB_NODELIST | head -n 1)
export MASTER_PORT=9901

worker_list=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | tr '\n' ' ')

echo "MASTER_ADDR="$MASTER_ADDR
echo "JobID: $SLURM_JOB_ID | Full list: $worker_list"

# OUTPUT of stage 2 script
export STAGE2_PATH="/model/experiments/0043_vila_step1/checkpoints/llm-jp-3-13b-instruct_siglip_mlp2xgelu_step-1_20240928"
# Final output checkpoint path
OUTPUT="llm-jp-3-13b-instruct_siglip_mlp2xgelu_step-2_tune_vision_20241006"
export OUTPUT_PATH=/model/experiments/0051_vila_extra/checkpoints/$OUTPUT

export NCCL_IB_SL=1
export CUDA_DEVICE_MAX_CONNECTIONS=1
#export NCCL_DEBUG=INFO
export NCCL_ASYNC_ERROR_HANDLING=1
#export CUDA_LAUNCH_BLOCKING=1

n_node=$SLURM_NNODES
export acc_step=1
export bs=$((16 / n_node / acc_step))
echo "number of nodes:" $n_node
echo "gradient accumulation steps:" $acc_step
echo "per device batch size:" $bs

source venv/bin/activate

srun --jobid $SLURM_JOBID bash -c 'python -m torch.distributed.run \
    --nproc_per_node $GPUS_PER_NODE --nnodes $SLURM_NNODES --node_rank $SLURM_PROCID \
    --master_addr $MASTER_ADDR --master_port $MASTER_PORT \
    llava/train/train_mem.py \
    --deepspeed ./scripts/zero3.json \
    --model_name_or_path $STAGE2_PATH \
    --version llmjp_v3 \
    --data_mixture llava_instruct_v1_5_en_subset+llava_instruct_ja+japanese_photos_conv+ja_vg_vqa+synthdog_ja_subset \
    --vision_tower google/siglip-so400m-patch14-384 \
    --mm_vision_select_feature cls_patch \
    --mm_projector mlp2x_gelu \
    --tune_vision_tower True \
    --tune_mm_projector True \
    --tune_language_model True \
    --mm_vision_select_layer -1 \
    --mm_use_im_start_end False \
    --mm_use_im_patch_token False \
    --image_aspect_ratio resize \
    --bf16 True \
    --output_dir $OUTPUT_PATH \
    --num_train_epochs 1 \
    --per_device_train_batch_size $bs \
    --per_device_eval_batch_size 4 \
    --gradient_accumulation_steps $acc_step \
    --evaluation_strategy "no" \
    --save_strategy "steps" \
    --save_steps 10000 \
    --save_total_limit 1 \
    --learning_rate 1e-4 \
    --weight_decay 0. \
    --warmup_ratio 0.03 \
    --lr_scheduler_type "cosine" \
    --logging_steps 1 \
    --tf32 True \
    --model_max_length 4096 \
    --gradient_checkpointing True \
    --dataloader_num_workers 16 \
    --lazy_preprocess True \
    --vflan_no_system_prompt True \
    --report_to wandb'
