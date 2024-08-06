model = dict(
    type="VideoMambaSuite",
    projection=dict(
        type="MambaProj",
        in_channels=2048,
        out_channels=512,
        arch=(2, 2, 5),  # layers in embed / stem / branch
        conv_cfg=dict(kernel_size=3),
        norm_cfg=dict(type="LN"),
        use_abs_pe=False,
        max_seq_len=2304,
        mamba_cfg=dict(kernel_size=4, drop_path_rate=0.3, use_mamba_type="dbm"),
    ),
    neck=dict(
        type="FPNIdentity",
        in_channels=512,
        out_channels=512,
        num_levels=6,
    ),
    rpn_head=dict(
        type="ActionFormerHead",
        num_classes=20,
        in_channels=512,
        feat_channels=512,
        num_convs=2,
        cls_prior_prob=0.01,
        prior_generator=dict(
            type="PointGenerator",
            strides=[1, 2, 4, 8, 16, 32],
            regression_range=[(0, 4), (4, 8), (8, 16), (16, 32), (32, 64), (64, 10000)],
        ),
        loss_normalizer=100,
        loss_normalizer_momentum=0.9,
        center_sample="radius",
        center_sample_radius=1.5,
        label_smoothing=0.0,
        loss=dict(
            cls_loss=dict(type="FocalLoss"),
            reg_loss=dict(type="DIOULoss"),
        ),
    ),
)
