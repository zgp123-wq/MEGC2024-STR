# Temporal-Informative Adapters in VideoMAE V2 and Multi-Scale Feature Fusion  for Micro-Expression Spotting-then-Recognition (ACM MM MEGC2024)


## ✨ Abstract

Micro-expressions are subtle facial movements that reveal hidden emotions, but their fleeting and involuntary nature poses significant challenges for detection. This paper introduces a novel approach addressing two critical tasks in micro-expression analysis: spotting and recognition. We integrate the VideoMAE V2 framework with a temporal information adapter and multi-scale feature fusion to enhance the performance of micro-expression spotting and recognition. Our method leverages the temporal information adapter to capture local temporal context within video frames, improving feature extraction efficiency. Additionally, we construct a multi-scale image pyramid to capture a range of motion features, from broad movements to subtle details. By combining these multi-scale features, our approach strengthens the model's capabilities in both micro-expression spotting and recognition. Our method effectively addresses issues related to environmental variations, involuntary facial movements, and dataset imbalance, leading to improved accuracy in Micro-Expression Spotting-then-Recognition. 

The architecture is shown as follows:
![frame](https://github.com/zgp123-wq/MEGC2024-STR/blob/main/figs/model.jpg)

## 🚀 Main Results

### ✨ MEGC 2024

![Leaderboard result](https://github.com/zgp123-wq/MEGC2024-STR/blob/main/figs/1722926399692.png)

## ⤴️ Fine-tuning with pre-trained models

- 

    ```
    sh finetune_cas_macro.sh
    ```
    just an example for fine-tuning, you might edit datasets.py, engine_for_finetuning.py, run_class_finetuning.py to suit your data
  
