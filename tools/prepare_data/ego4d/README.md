# Data Preparation for Ego4D-Moment Query

## Download Annotations

You can download the annotation by
```bash
bash download_annotation.sh
```

Alternately, you can prepare the annotations by yourself. After downloading the original annotations from the Ego4D website, you can run the following command to convert them.

```bash
python tools/prepare_data/ego4d/convert_ego4d_anno.py \
  ego4d/v2/annotations \
  data/ego4d/annotations/ego4d_v2_220429.json
```

## Download Pre-extracted Features

Please put the downloaded feature under the path: `data/ego4d/features/`.


We provide the following pre-extracted features for Ego4d-MQ:

|   Feature    |                                                Url                                                 |  Backbone  |                  Feature Extraction Setting                  |
| :----------: | :------------------------------------------------------------------------------------------------: | :--------: | :----------------------------------------------------------: |
|    EgoVLP    | [Google Drive](https://drive.google.com/file/d/1_ys0fUX9FJlUeHBJ4-Fqxf-Ip3khalHf/view?usp=sharing) |   EgoVLP   | 30 fps,  snippet_stride=16, clip_length=16, frame_interval=1 |
|   SlowFast   | [Google Drive](https://drive.google.com/file/d/1Im27Ga9JWhjIqp6L9mQyu1aMGjdo6iNV/view?usp=sharing) |  SlowFast  | 30 fps,  snippet_stride=16, clip_length=16, frame_interval=1 |
| InternVideo1 | [Google Drive](https://drive.google.com/file/d/18oqhrSHBFrKIAGM2mWzZZZBIufwVSUQ5/view?usp=sharing) | VideoMAE-L | 30 fps,  snippet_stride=8, clip_length=16, frame_interval=1  |

## Download Raw Videos

Note that we are not allowed to distribute the Ego4D videos due to the license requirement. You can download the videos from [Ego4D website](https://ego4d-data.org/). Then, you can use the following command to trim the raw videos into MQ-clips.
```bash
python tools/prepare_data/ego4d/accurate_trim_MQ.py \
  ego4d_data/v2/annotations \
  ego4d_data/v1/full_scale \
  data/ego4d/raw_data/MQ_data/mq_videos_short320
```
You can also add `--part 0 --total 4` to the command to split and speed up the trimming process .


## Citation

```BibTeX
@inproceedings{grauman2022ego4d,
  title={Ego4d: Around the world in 3,000 hours of egocentric video},
  author={Grauman, Kristen and Westbury, Andrew and Byrne, Eugene and Chavis, Zachary and Furnari, Antonino and Girdhar, Rohit and Hamburger, Jackson and Jiang, Hao and Liu, Miao and Liu, Xingyu and others},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={18995--19012},
  year={2022}
}
```