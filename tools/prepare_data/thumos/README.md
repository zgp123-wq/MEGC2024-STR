# Data Preparation for THUMOS14

## Download Annotations

You can download the annotation by
```bash
bash download_annotation.sh
```
The annotation should be in `data/thumos-14/annotations/`.

- Following previous work such as G-TAD/VSGN, two videos are removed from the THUMOS14 validation set. (`video_test_0000270` due to wrong annotations, `video_test_0001292` due to empty annotations). Therefore, there are total 211 videos left in test subset. In this codebase, we use this annotation file to conduct all THUMOS-related experiments for a fair comparison.


## Download Pre-extracted Features

Please put the downloaded feature under the path: `data/thumos-14/features/`.


We provide the following pre-extracted features for THUMOS14:

|     Feature     |                                                                          Url                                                                           |         Backbone         |             Feature Extraction Setting             |
| :-------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------: | :----------------------: | :------------------------------------------------: |
|       i3d       |                           [Google Drive](https://drive.google.com/file/d/1bxpfdFRQNCFlQ39aIocLjSt0C6_M6t6N/view?usp=sharing)                           |     I3D (two stream)     |    snippet_stride=4, extracted by ActionFormer     |
|       tsn       |                           [Google Drive](https://drive.google.com/file/d/1z5s8WTwZCXkGFRCT0jhyJhcJEGcGGcTx/view?usp=sharing)                           |     TSN (two stream)     |        snippet_stride=1, extracted by G-TAD        |
|  slowfast_r50   |                           [Google Drive](https://drive.google.com/file/d/1ORcNmUcPXezDtOfCPawuTf6UkiQ--PQv/view?usp=sharing)                           |    SlowFast-R50-8x8x1    | snippet_stride=4, clip_length=32, frame_interval=1 |
|  slowfast_r101  |                           [Google Drive](https://drive.google.com/file/d/1L5WT2Qo-ZZ2sBtgv4uYXUHE8w5CGy5dy/view?usp=sharing)                           |   SlowFast-R101-8x8x1    | snippet_stride=4, clip_length=32, frame_interval=1 |
|   videomae_b    |                           [Google Drive](https://drive.google.com/file/d/1qI20zPzjJ5rHz1G9QyJEksfw-QW9oSVu/view?usp=sharing)                           |    VideoMAE-B-16x4x1     | snippet_stride=4, clip_length=16, frame_interval=1 |
|   videomae_l    |                           [Google Drive](https://drive.google.com/file/d/1-qHD6s8w21TCeExp9DPtAGX409OjwW18/view?usp=sharing)                           |    VideoMAE-L-16x4x1     | snippet_stride=4, clip_length=16, frame_interval=1 |
|   videomae_h    | [InternVideo Repo](https://github.com/OpenGVLab/InternVideo/tree/main/Downstream/Temporal-Action-Localization#to-reproduce-our-results-of-internvideo) |  VideoMAE-H-K700-16x4x1  | snippet_stride=4, clip_length=16, frame_interval=1 |
|  videomaev2_g   |                           [Google Drive](https://drive.google.com/file/d/1FRoCz_ZS13faRLN6ocfwghsmIsENLz7_/view?usp=sharing)                           | VideoMAEv2-g-K710-16x4x1 | snippet_stride=4, clip_length=16, frame_interval=1 |
| internvideo2_6b |           [Official Repo](https://github.com/OpenGVLab/video-mamba-suite/blob/main/video-mamba-suite/temporal-action-localization/README.md)           |     InternVideo2-6B      | snippet_stride=4, clip_length=16, frame_interval=1 |

## Download Raw Videos

Please put the downloaded video under the path: `data/thumos-14/raw_data/`.

You can download the raw video from [official website](https://www.crcv.ucf.edu/THUMOS14/download.html), or download from this [Google Drive](https://drive.google.com/file/d/1cbwDvIk4DsM5uSZJpGDfjGu4ZeZhftgK/view?usp=sharing).

## Citation

```BibTeX
@misc{THUMOS14,
    author = {Jiang, Y.-G. and Liu, J. and Roshan Zamir, A. and Toderici, G. and Laptev,
    I. and Shah, M. and Sukthankar, R.},
    title = {{THUMOS} Challenge: Action Recognition with a Large
    Number of Classes},
    howpublished = "\url{http://crcv.ucf.edu/THUMOS14/}",
    Year = {2014}
}
```