from utils import *
import threading
import time

def dld_index_2(index_2):
    Semaphore.acquire()
    index_2_4 = index_2.zfill(4)
    # print(index_2)
    old_dld_path = local_path_sort + '/' + index_2_4
    if index_2_4 in index_2_list:
        new_dld_path = local_path_sort + '/' + str(name_list[index_2_list.index(index_2_4)])
        dld_path = new_dld_path
        if os.path.exists(old_dld_path):
            os.rename(old_dld_path, new_dld_path)
    else:
        dld_path = old_dld_path
    
    for index_1 in range(1,7):
        # index_1: quality of the skin [1, 6]
        # print('\t' + str(index_1))
        indicator = 0
        for index_3 in range(1,10):
            skin_number = str(index_1) + index_2 + str(index_3).zfill(2)
            # for dynamic skin on pc index_1 plus 2
            skin_number_plus2 = str(index_1 + 2) + index_2 + str(index_3).zfill(2)

            # try to download default type of file
            if folder_list[0] is not None:
                file_path = dld_path + '/' + folder_list[0]
            else:
                file_path = dld_path + '/'
            if not dld(file_path.replace('skin_number_plus2', skin_number_plus2).replace('skin_number', skin_number), file_name_list[0].replace('skin_number_plus2', skin_number_plus2).replace('skin_number', skin_number), url_list[0].replace('skin_number_plus2', skin_number_plus2).replace('skin_number', skin_number)):
                # if the default type of file does not exist, indicator ++
                indicator = indicator + 1
            else:
                indicator = 0
            
            # if the 1bbbb01 file does not exist
            if (indicator > 0) & (index_1 == 1) & (index_3 == 1):
                # index_2 is not valid, return None and try another index_2
                Semaphore.release()
                return None

            # if the abbbb01 file does not exist
            # if (indicator > 0) & (index_3 == 1):
            #     # index_1 is not valid, try next index_1
            #     break

            # if the abbbbcc file does not exist
            # if (indicator > 0):
            #     # index_3 is not valid, try next index_3
            #     continue

            # if indicator above certain value
            if (indicator > 2):
                break

            # try to download the rest types of the files
            for file_type_index, file_name in enumerate(file_name_list[1:]):
                if folder_list[file_type_index + 1] is not None:
                    file_path = dld_path + '/' + folder_list[file_type_index + 1]
                else:
                    file_path = dld_path + '/'
                url = url_list[file_type_index + 1]
                dld(file_path.replace('skin_number_plus2', skin_number_plus2).replace('skin_number', skin_number), file_name.replace('skin_number_plus2', skin_number_plus2).replace('skin_number', skin_number), url.replace('skin_number_plus2', skin_number_plus2).replace('skin_number', skin_number))

    Semaphore.release()


# -------------------------------------------------------------------------------------

# Settings
# Download path
# local_path = os.getcwd() + '\\download'
local_path = '.\\download'

# Number of download threads
max_connections = 12

# Create the sort folder
local_path_sort = local_path + '\\sort'
mkdir(local_path_sort)
# Create a Bounded Semaphore
Semaphore = threading.BoundedSemaphore(max_connections)

# Get infomation about characters and file samples to be downloaded
(name_list, index_2_list) = get_sort_info(local_path)
(url_list, folder_list, file_name_list) = get_example_info(local_path)

# dld_index_2('031')

# Define a list, where all download threads are put into
threads = []
# Put all threads into the list
index_2_start = 1
index_2_end = 10000
index_2_len = index_2_end - index_2_start
for index_2 in range(index_2_start, index_2_end):
    threads.append(threading.Thread(target=dld_index_2, args=(str(int(index_2)).zfill(3),)))
# Use start() method to start the threads
for thread in threads:
    thread.start()
# Use join() method to let the main thread waiting for the finish of subthreads
# for thread in threads:
#     thread.join()

# Progress Bar
print('Download Progress:')
start_time = time.perf_counter()
while len(threading.enumerate()) > 1:
    time.sleep(0.5)
    current_time = time.perf_counter()
    print_progress(index_2_len - (len(threading.enumerate()) - 1), index_2_len, current_time - start_time)
current_time = time.perf_counter()
print_progress(index_2_len - (len(threading.enumerate()) - 1), index_2_len, current_time - start_time)
print('\n')
