from openpyxl import load_workbook
import os
import shutil


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

def get_sort_info_female(local_path): 
    index_2_list = []
    name_list = []
    wb = load_workbook(filename = local_path + '/' + 'sort.xlsx')
    ws = wb['Sheet1']
    rows = ws.rows
    for row in rows:
        line = [col.value for col in row]
        
        if line[2] == None:
            name = line[3]
        else:
            name = line[2] + '·' + line[3]
        name = str(name)
        name = str(line[0]).zfill(4) + ' - ' + name.replace(u'\u3000',u'')

        if line[4] == '女':
            index_2_list.append(str(line[0]).zfill(4))
            name_list.append(name)

    return name_list, index_2_list


local_path = '.\\download'
local_path_sort = local_path + '\\sort'

txt_mobile = local_path + '/' + 'female_mobile.txt'
txt_mobile_pro = local_path + '/' + 'female_mobile_pro.txt'
txt_mobile_all = local_path + '/' + 'female_mobile_all.txt'
txt_pc = local_path + '/' + 'female_pc.txt'
txt_pc_skel = local_path + '/' + 'female_pc_skel.txt'

(name_list, index_2_list) = get_sort_info_female(local_path)

with open(txt_mobile, 'w') as f_mobile, open(txt_mobile_pro, 'w') as f_mobile_pro, open(txt_mobile_all, 'w') as f_mobile_all, open(txt_pc, 'w') as f_pc, open(txt_pc_skel, 'w') as f_pc_skel:  
    f_mobile.write('[')
    f_mobile_pro.write('[')
    f_mobile_all.write('[')
    f_pc.write('[')
    f_pc_skel.write('[')
    character_folders = os.listdir(local_path_sort)
    for character_folder in character_folders:
        # print(character_folder)
        if character_folder in name_list:
            female_files = os.listdir(local_path_sort + '/' + character_folder)
            for female_file in female_files:
                full_path = local_path_sort + '/' + character_folder + '/' + female_file + '/'
                relative_path = '/' + character_folder + '/' + female_file + '/'
                if os.path.isdir(full_path):
                    # print(relative_path)
                    if female_file.endswith('_mobile'):
                        female_file_subs = os.listdir(full_path)
                        if 'beijing.skel' in female_file_subs:
                            f_mobile.write('"' + relative_path + '"')
                            f_mobile.write(',')
                            f_mobile.write('\n')
                            f_mobile_all.write('"' + relative_path + '"')
                            f_mobile_all.write(',')
                            f_mobile_all.write('\n')
                    elif female_file.endswith('_mobile_pro'):
                        female_file_subs = os.listdir(full_path)
                        if 'beijing.skel' in female_file_subs:
                            f_mobile_pro.write('"' + relative_path + '"')
                            f_mobile_pro.write(',')
                            f_mobile_pro.write('\n')
                            f_mobile_all.write('"' + relative_path + '"')
                            f_mobile_all.write(',')
                            f_mobile_all.write('\n')
                    elif female_file.endswith('_pc'):
                        female_file_subs = os.listdir(full_path)
                        if 'beijing.sk' in female_file_subs:
                            f_pc.write('"' + relative_path + '"')
                            f_pc.write(',')
                            f_pc.write('\n')
                        elif 'beijing.skel' in female_file_subs:
                            f_pc_skel.write('"' + relative_path + '"')
                            f_pc_skel.write(',')
                            f_pc_skel.write('\n')
    f_mobile.write(']')
    f_mobile_pro.write(']')
    f_pc.write(']')
    f_pc_skel.write(']')


txt_all = local_path + '/' + 'files.txt'
character_folders = os.listdir(local_path_sort)
idx = 0
with open(txt_all, 'w') as f: 
    for character_folder in character_folders:
        female_files = os.listdir(local_path_sort + '/' + character_folder)
        for female_file in female_files:
            idx = idx + 1
            full_path = local_path_sort + '/' + character_folder + '/' + female_file
            relative_path = '/' + character_folder + '/' + female_file
            # f.write(relative_path)
            # f.write('\n')
        f.write(character_folder + ':' + str(idx))
        f.write('\n')