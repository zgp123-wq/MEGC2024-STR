_base_ = [
    "../_base_/datasets/activitynet-1.3/features_tsp_resize.py",  # dataset config
    "../_base_/models/bmn.py",  # model config
]

data_path = "data/activitynet-1.3/features/anet_tsn_npy_unresize/"
block_list = "data/activitynet-1.3/features/anet_tsn_npy_unresize/missing_files.txt"
dataset = dict(
    train=dict(data_path=data_path, block_list=block_list),
    val=dict(data_path=data_path, block_list=block_list),
    test=dict(data_path=data_path, block_list=block_list),
)

solver = dict(
    train=dict(batch_size=16, num_workers=4),
    val=dict(batch_size=16, num_workers=4),
    test=dict(batch_size=16, num_workers=4),
    clip_grad_norm=1,
)

optimizer = dict(type="Adam", lr=1e-3, weight_decay=1e-4, paramwise=True)
scheduler = dict(type="MultiStepLR", milestones=[7], gamma=0.1, max_epoch=10)

inference = dict(test_epoch=7, load_from_raw_predictions=False, save_raw_prediction=False)
post_processing = dict(
    nms=dict(
        use_soft_nms=True,
        sigma=0.5,
        max_seg_num=100,
        min_score=0.01,
        multiclass=False,
        voting_thresh=0.95,  #  set 0 to disable
    ),
    external_cls=dict(
        type="CUHKANETClassifier",
        path="data/activitynet-1.3/classifiers/cuhk_val_simp_7.json",
        topk=2,
    ),
    save_dict=False,
)

workflow = dict(
    logging_interval=200,
    checkpoint_interval=1,
    val_loss_interval=1,
    val_eval_interval=1,
    val_start_epoch=7,
)

work_dir = "exps/anet/bmn_tsn_128"
