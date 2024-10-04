from dataclasses import dataclass, field


@dataclass
class Dataset:
    dataset_name: str
    dataset_type: str = field(default="torch")
    data_path: str = field(default=None, metadata={"help": "Path to the training data."})
    meta_path: str = field(default=None, metadata={"help": "Path to the meta data for webdataset."})
    image_path: str = field(default=None, metadata={"help": "Path to the training image data."})
    description: str = field(
        default=None,
        metadata={
            "help": "Detailed desciption of where the data is from, how it is labelled, intended use case and the size of the dataset."
        },
    )
    test_script: str = (None,)
    maintainer: str = (None,)


DATASETS = {}

import warnings


def add_dataset(dataset):
    if dataset.dataset_name in DATASETS:
        # make sure the data_name is unique
        warnings.warn(f"{dataset.dataset_name} already existed in DATASETS. Make sure the name is unique.")
    assert "+" not in dataset.dataset_name, "Dataset name cannot include symbol '+'."
    DATASETS.update({dataset.dataset_name: dataset})



def register_datasets_mixtures():

    # Align
    llava_1_5_mm_align = Dataset(
        dataset_name='llava_1_5_align',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-Pretrain/LLaVA-CC3M-Pretrain-595K.json',
        image_path='./playground/data/LLaVA-Pretrain/images'
    )
    add_dataset(llava_1_5_mm_align)

    llava_1_5_mm_align_en = Dataset(
        dataset_name='llava_1_5_mm_align_en',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-Pretrain/blip_laion_cc_sbu_558k.json',
        image_path='./playground/data/LLaVA-Pretrain-JA/images'
    )
    add_dataset(llava_1_5_mm_align_en)

    llava_1_5_mm_align_ja = Dataset(
        dataset_name='llava_1_5_mm_align_ja',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-Pretrain-JA/llava_pretrain_blip_laion_cc_sbu_558k_ja.jsonl',
        image_path='./playground/data/LLaVA-Pretrain-JA/images'
    )
    add_dataset(llava_1_5_mm_align_ja)

    llm_jp_mm_pair_step0_558k = Dataset(
        dataset_name='llm_jp_mm_pair_step0_558k',
        dataset_type='torch',
        data_path='./playground/data/alt_pair_ja/llm-jp_mm_pair_step0_558k.json',
        image_path='./playground/data/alt_pair_ja/image_step0'
    )
    add_dataset(llm_jp_mm_pair_step0_558k)

    # Pretrain
    coyo_25m = Dataset(
        dataset_name='coyo',
        dataset_type='coyo',
        data_path='./playground/data/coyo-700m/pkl02-split')
    add_dataset(coyo_25m)

    mmc4core = Dataset(
        dataset_name='mmc4core',
        dataset_type='mmc4',
        data_path='./playground/data/mmc4-core/pkl-core')
    add_dataset(mmc4core)

    sharegpt4v_pretrain = Dataset(
        dataset_name="sharegpt4v_pretrain",
        dataset_type="torch",
        data_path="./playground/data/ShareGPT4V/jason-filter-share-captioner_coco_lcs_sam_1246k_1107.json",
        image_path="./playground/data/ShareGPT4V/data",
    )
    add_dataset(sharegpt4v_pretrain)

    coyo_6m = Dataset(
        dataset_name='coyo_6m',
        dataset_type='coyo',
        data_path='./playground/data/coyo-700m/pkl03-split')
    add_dataset(coyo_6m)

    mmc4core_6m = Dataset(
        dataset_name='mmc4core_6m',
        dataset_type='mmc4',
        data_path='./playground/data/mmc4-core/pkl-core-limit-tokens')
    add_dataset(mmc4core_6m)

    llm_jp_mm_pair_step1_6m = Dataset(
        dataset_name='llm_jp_mm_pair_step1_6m',
        dataset_type='coyo',
        data_path='./playground/data/alt_pair_ja/pkl02')
    add_dataset(llm_jp_mm_pair_step1_6m)

    llm_jp_mm_interleaved_step1_6m = Dataset(
        dataset_name='llm_jp_mm_interleaved_step1_6m',
        dataset_type='mmc4',
        data_path='./playground/data/mmc4_ja/pkl-limit-tokens')
    add_dataset(llm_jp_mm_interleaved_step1_6m)

    # SFT
    sharegpt4v_gpt4_100k = Dataset(
        dataset_name="sharegpt4v_gpt4_100k",
        dataset_type="torch",
        data_path="./playground/datasharegpt_video/ShareGPT4V/sharegpt4v_instruct_gpt4-vision_cap100k.json",
        image_path="./playground/datasharegpt_video/ShareGPT4V/data",
    )
    add_dataset(sharegpt4v_gpt4_100k)

    llava_instruct = Dataset(
        dataset_name="llava_instruct",
        dataset_type="torch",
        data_path="./playground/data/llava_instruct_150k_zh.jsonl",
        image_path="./playground/data/coco",
        description="",
    )
    add_dataset(llava_instruct)

    llava_instruct_en = Dataset(
        dataset_name='llava_instruct_en',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-Instruct-150K/llava_instruct_150k.json',
        image_path='./playground/data/coco/train2017'
    )
    add_dataset(llava_instruct_en)
    
    llava_instruct_ja_translate = Dataset(
        dataset_name='llava_instruct_ja_translate',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-Instruct-150K-JA/llava_instruct_150k_ja.jsonl',
        image_path='./playground/data/coco/train2017'
    )
    add_dataset(llava_instruct_ja_translate)

    llava_instruct_v1_5_en = Dataset(
        dataset_name='llava_instruct_v1_5_en',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-Instruct-150K/llava_v1_5_mix665k.json',
        image_path='./playground/data'
    )
    add_dataset(llava_instruct_v1_5_en)

    llava_instruct_v1_5_ja_translate = Dataset(
        dataset_name='llava_instruct_v1_5_ja_translate',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-v1.5-Instruct-620K-JA/llava_v1_5_instruct_620k_ja_v2.jsonl',
        image_path='./playground/data'
    )
    add_dataset(llava_instruct_v1_5_ja_translate)

    llava_instruct_v1_5_en_subset = Dataset(
        dataset_name='llava_instruct_v1_5_en_subset',
        dataset_type='torch',
        data_path='./playground/data/LLaVA-Instruct-150K/llava_v1_5_subset_358k.json',
        image_path='./playground/data'
    )
    add_dataset(llava_instruct_v1_5_en_subset)

    llava_instruct_ja = Dataset(
        dataset_name='llava_instruct_ja',
        dataset_type='torch',
        data_path='./playground/data/llava_instruct_ja/llava_instruct_ja_156k.json',
        image_path='./playground/data'
    )
    add_dataset(llava_instruct_ja)

    japanese_photos_conv = Dataset(
        dataset_name='japanese_photos_conv',
        dataset_type='torch',
        data_path='./playground/data/japanese-photos/japanese_photos_conv_12k.json',
        image_path='./playground/data/japanese-photos/images'
    )
    add_dataset(japanese_photos_conv)

    ja_vg_vqa = Dataset(
        dataset_name='ja_vg_vqa',
        dataset_type='torch',
        data_path='./playground/data/ja-vg-vqa/ja-vg-vqa_instruct_99k.json',
        image_path='./playground/data'
    )
    add_dataset(ja_vg_vqa)

    synthdog_ja_subset = Dataset(
        dataset_name='synthdog_ja_subset',
        dataset_type='torch',
        data_path='./playground/data/synthdog-ja/synthdog_ja_102k.json',
        image_path='./playground/data'
    )
    add_dataset(synthdog_ja_subset)

    sharegpt4v_sft = Dataset(
        dataset_name='sharegpt4v_sft',
        dataset_type='torch',
        data_path='./playground/data/sharegpt4v/sharegpt4v_mix738k_remove_sa.json',
        image_path='./playground/data'
    )
    add_dataset(sharegpt4v_sft)

    dvqa_train_200k = Dataset(
        dataset_name="dvqa_train_200k",
        dataset_type="torch",
        data_path="./playground/data/dvqa_train_200k.jsonl",
        image_path="./playground/data/dvqa",
        description="",
    )
    add_dataset(dvqa_train_200k)

    chartqa_train_18k = Dataset(
        dataset_name="chartqa_train_18k",
        dataset_type="torch",
        data_path="./playground/data/chartqa_train_18k.jsonl",
        image_path="./playground/data/chartqa",
        description="",
    )
    add_dataset(chartqa_train_18k)

    ai2d_train_12k = Dataset(
        dataset_name="ai2d_train_12k",
        dataset_type="torch",
        data_path="./playground/data/ai2d_train_12k.jsonl",
        image_path="./playground/data/ai2d",
        description="",
    )
    add_dataset(ai2d_train_12k)

    docvqa_train_10k = Dataset(
        dataset_name="docvqa_train_10k",
        dataset_type="torch",
        data_path="./playground/data/docvqa_train_10k.jsonl",
        image_path="./playground/data/docvqa",
        description="",
    )
    add_dataset(docvqa_train_10k)

    geoqa = Dataset(
        dataset_name="geoqa",
        dataset_type="torch",
        data_path="./playground/data/geoqa+.jsonl",
        image_path="./playground/data/geoqa+",
        description="",
    )
    add_dataset(geoqa)

    synthdog_en = Dataset(
        dataset_name="synthdog_en",
        dataset_type="torch",
        data_path="./playground/data/synthdog_en.jsonl",
        image_path="./playground/data/synthdog-en",
        description="",
    )
    add_dataset(synthdog_en)

    vflan = Dataset(
        dataset_name='vflan',
        dataset_type='vflan',
        data_path='./playground/data/vlm-flan-clean-text1m-nosqa-sharded'
    )
    add_dataset(vflan)


    scienceqa = Dataset(
        dataset_name="scienceqa",
        dataset_type="torch",
        data_path="./playground/data/scienceqa/scienceqa_train_12k.json",
        image_path="./playground/data/scienceqa/images",
    )
    add_dataset(scienceqa)

    
    sherlock = Dataset(
        dataset_name="sherlock",
        dataset_type="torch",
        data_path="./playground/data/sherlock/processed/sherlock_317k.json",
        image_path="./playground/data/sherlock/images",
    )
    add_dataset(sherlock)
    math = Dataset(
        dataset_name="math",
        dataset_type="vflan",
        data_path="./playground/data/math",
    )
    add_dataset(math)

    wit_subset = Dataset(
        dataset_name="wit_subset",
        dataset_type="torch",
        data_path="./playground/data/WIT/wit_1_8m/wit_processed_538k.json",
        image_path="./playground/data/WIT/wit_1_8m/images"
    )
    add_dataset(wit_subset)

    youcook2 = Dataset(
        dataset_name="youcook2",
        dataset_type="torch",
        data_path="./playground/data/youcook2/youcook_filtered_v3.json",
        image_path="./playground/data/youcook2/video_data_clipped",
    )
    add_dataset(youcook2)
    
    vatex = Dataset(
        dataset_name="vatex",
        dataset_type="torch",
        data_path="./playground/data/vatex/vatex_filtered_v3.json",
        image_path="./playground/data/vatex/videos_clipped",
    )
    add_dataset(vatex)

    video_chatgpt = Dataset(
        dataset_name="video_chatgpt",
        dataset_type="torch",
        data_path="./playground/data/Video_ChatGPT/VideoInstruct-100K/VideoInstruct100K.json",
        image_path="./playground/data/Video_ChatGPT/activitynet_videos/",
    )
    add_dataset(video_chatgpt)

    shot2story_shotonly = Dataset(
        dataset_name="shot2story_shotonly",
        dataset_type="torch",
        data_path="./playground/data/shot2story/shot2story_shotonly.json",
        image_path="./playground/data/shot2story/Shot2Story/data/videos_extracted",
    )
    add_dataset(shot2story_shotonly)

    sharegpt_video = Dataset(
        dataset_name="sharegpt_video",
        dataset_type="torch",
        data_path="./playground/data/sharegpt_video/video_caption_pretrain.json",
        image_path="./playground/data/sharegpt_video/videos",
    )
    add_dataset(sharegpt_video)




    