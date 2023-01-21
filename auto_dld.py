import os

while True:
    code_path = os.getcwd() + '\\'

    cmd = 'python ' + '"' + code_path + '0-dld_from_nothing_update.py' + '"'
    os.system(cmd)

    cmd = 'python ' + '"' + code_path + '6-extract_female_dragonbones_list_relative.py' + '"'
    os.system(cmd)

    
