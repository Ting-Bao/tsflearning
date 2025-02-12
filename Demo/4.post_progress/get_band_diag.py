import os, json
# run @ MPI raven by baot

calc_src_dir = './sparse_calc_diag.jl'

# get current working directory
working_path = os.getcwd()

# must-have files in working_path:
# rlat.dat, orbital_types.dat, site_positions.dat, hamiltonians_pred.h5, overlaps.h5

# input info for band prediction
E_Fermi_Hartree = -0.15058399547659 # from 3.48 DFT # grep Chemical openmx.out !!!
E_Fermi_eV = E_Fermi_Hartree*27.21138602

# if load fermi energy from info.json
load_infojson = True
if load_infojson == True:
    print("load fermi energy from info.json")
    with open('info.json', 'r') as f:
        tmp = json.load(f)
        E_Fermi_eV = tmp['fermi_level']

lowest_band = -0.55
max_inter = 300
num_band = 50

# kp_path = ["15 0.000 0.000 0.000  0.000 0.500 0.000  Γ Y",
#            "15 0.000 0.500 0.000  0.500 0.500 0.000  Y M",
#            "15 0.500 0.500 0.000  0.500 0.000 0.000  M X",
#            "15 0.500 0.000 0.000  0.000 0.000 0.000  X Γ"]  # square or rectangular lattice
# kp_path = ["15 0.5 0.0 0.0 0.0 0.0 0.0 M Γ",
#            "15 0.0 0.0 0.0 0.666666667 0.333333333 0.0 Γ K",
#            "15 0.666666667 0.333333333 0.0 0.5 0.0 0.0 K M"]  # triangular lattice

# 120degree
kp_path = ["12 0.0 0.0 0.0 0.5 0.0 0.0 G M",
           "12 0.5 0.0 0.0 0.333333333 0.33333333 0.0 M K",
           "12 0.333333333 0.333333333 0.0 0.0 0.0 0.0 K G"]
header = f'export OMP_NUM_THREADS=64\nexport JULIA_NUM_THREADS=64\nexport LD_LIBRARY_PATH=${{LD_LIBRARY_PATH}}:/home/lihe/local/usr/lib64:/home/lihe/lib\n'


bash_cmd = ''
for i in range(1,36+1):
# for i in range(45+1):  # index of k points, change when use !!!
    if i == 0:
        band_config_json = {"calc_job": "band",
                            "which_k": -1,
                            "fermi_level": E_Fermi_eV,
                            "lowest_band": lowest_band,
                            "max_iter": max_inter,
                            "num_band": num_band,
                            "k_data": kp_path}
        config_path = os.path.join(working_path, 'band_config.json')
        with open(config_path, 'w') as jsonf0:
            json.dump(band_config_json, jsonf0)
        os.system(header + f'julia {calc_src_dir} --input_dir {working_path} --output_dir {working_path} --config {config_path}')
        print('Finish get jld and Band file')
    else:
        band_config_json = {"calc_job": "band",
                            "which_k": i,
                            "fermi_level": E_Fermi_eV,
                            "lowest_band": lowest_band,
                            "max_iter": max_inter,
                            "num_band": num_band,
                            "k_data": kp_path}
        band_idx = f'{i}'
        config_file_path = os.path.join(working_path, 'egval_k', band_idx)
        os.makedirs(config_file_path, exist_ok=True)

        with open(os.path.join(config_file_path, 'band_config.json'), 'w') as jsonf:
            json.dump(band_config_json, jsonf)

        # bash_cmd += f'julia16 {calc_src_dir} --input_dir {working_path} --output_dir {config_file_path} --config {config_file_path}/band_config.json &\n'
        bash_cmd += f'export OMP_NUM_THREADS=4 && export JULIA_NUM_THREADS=4 && julia {calc_src_dir} --input_dir {working_path} --output_dir {config_file_path} --config {config_file_path}/band_config.json >> stdoutput \n'

with open('./cmd_all.sh','w',encoding='utf-8') as fp:
    fp.write(bash_cmd)
    print("run this python file first to get the jld file\n Writing all cmds to cmd_all.sh!\n")
    print("to sperate to several file, use \n split -l [lines_each_file] cmd_all.sh -d -a 2 cmd_")


