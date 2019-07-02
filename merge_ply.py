# import necessary module
import numpy as np
from plyfile import PlyData, PlyElement
import os

f_list = os.listdir("./")
# print f_list

vertex = []
for i in f_list:
	# os.path.splitext():分离文件名与扩展名
    if os.path.splitext(i)[1] == '.ply':
        print(i)
        plydata = PlyData.read(i)
        if not len(vertex):
            vertex = plydata['vertex'].data
        else:
            a = plydata['vertex'].data
            vertex = np.concatenate((vertex, a))

print(type(vertex))
el = PlyElement.describe(vertex, 'vertex')
PlyData([el]).write('merge_binary.ply')