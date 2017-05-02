# coding: utf-8
import sys

import json


log_file = "/media/zh/E/scene/places365/docker/sougou.log"
with open(log_file, 'r') as file_object:
    lines = file_object.readlines()
    for line in lines:
        filename = line.split('\n')
        print(filename[0])



# with open('thefile.txt', 'w') as file_object:
#     x = []
#     g = os.walk(img_dir)
#     for path,d,filelist in g:
#         for filename in filelist:
#             if filename.endswith('jpg'):
#                 f = os.path.join(path, filename)
#                 f = f + '\n'
#                 x.append(f)
#     print(x)
#     file_object.writelines(x)
# file_object.close()