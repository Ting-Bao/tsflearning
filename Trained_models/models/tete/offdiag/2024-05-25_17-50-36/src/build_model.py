from deephe3_1 import Net
net = Net(
    index_to_Z=[42, 52],
    irreps_embed_node='64x0e',
    irreps_edge_init='64x0e',
    irreps_sh='1x0e+1x1o+1x2e+1x3o+1x4e+1x5o',
    irreps_mid_node='64x0e+32x1o+32x2e+16x3o+8x4e+4x5o',
    irreps_post_node='64x0e+32x1o+32x2e+16x3o+8x4e+4x5o+32x1e',
    irreps_out_node='1x0e',
    irreps_mid_edge='64x0e+32x1o+32x2e+16x3o+8x4e+4x5o',
    irreps_post_edge='40x0o+28x0e+96x1o+68x1e+88x2o+76x2e+48x3o+44x3e+16x4o+12x4e+4x5e',
    irreps_out_edge='1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e',
    num_block=3,
    r_max=9.0,
    use_sc=True,
    no_parity=False,
    use_sbf=False,
    only_ij=False,
    if_sort_irreps=False
)
