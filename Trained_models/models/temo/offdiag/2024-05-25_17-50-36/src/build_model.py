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
    irreps_post_edge='36x0o+24x0e+84x1o+54x1e+72x2o+56x2e+36x3o+30x3e+12x4o+6x4e+2x5e',
    irreps_out_edge='1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x0e+1x1e+1x0e+1x1e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x2e+1x1e+1x2e+1x3e+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x1o+1x0o+1x1o+1x2o+1x0e+1x1e+1x2e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x2e+1x1e+1x2e+1x3e+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x1o+1x2o+1x3o+1x0o+1x1o+1x2o+1x1o+1x2o+1x3o+1x2o+1x3o+1x4o+1x0e+1x1e+1x2e+1x3e+1x4e+1x1e+1x0e+1x1e+1x2e+1x1e+1x2e+1x3e+1x2e+1x3e+1x4e+1x3e+1x4e+1x5e',
    num_block=3,
    r_max=9.0,
    use_sc=True,
    no_parity=False,
    use_sbf=False,
    only_ij=False,
    if_sort_irreps=False
)
