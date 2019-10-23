# -*- coding: UTF-8 -*-
import os
import shutil
import time
import math

"""
author: 拯救地球的程咬金
time:   2019-10-23 16:00
"""

def classfity(path):
    start = time.time()
    for root, dirs, files in os.walk(path):
        time_name_dict = {}
        for file in files:
            m_time = time.localtime(os.stat(os.path.join(path, file)).st_mtime)
            time_name_dict[file] = time.strftime("%Y-%m-%d %H:%M",m_time)
        #然后根据dict中的value值进行排序
        files_sorted = sorted(time_name_dict.items(), key=lambda x: x[1])
        for i in range(len(files_sorted)):
            if (files_sorted[i][0][-3:] == 'jpg') or (files_sorted[i][0][-3:] == 'png') or (files_sorted[i][0][-3:] == 'JPG') or (files_sorted[i][0][-3:] == 'csv'):
                file_path = root + '/' + files_sorted[i][0]
                #配置新建文件夹的编号
                num_1 = i/10
                j = math.floor(num_1)
                k = "YJ%03d" %(j+1)
                file_num_name = path + str(k)
                if os.path.isdir(file_num_name):
                    new_file_path = path + '/' + k + '/' + files_sorted[i][0]
                    shutil.copy(file_path, new_file_path)
                else:
                    os.mkdir(file_num_name)
                    new_file_path = path + '/' + k + '/' + files_sorted[i][0]
                    shutil.copy(file_path, new_file_path)
    print('所有文件分割完毕！')
    end = time.time()
    print("运行时间为：%.2f秒" % (end - start))

if __name__ == '__main__':
    # path = '/data/picture_classfity/images/'
    path = input("请输入您要分割的文件夹地址：")
    classfity(path)