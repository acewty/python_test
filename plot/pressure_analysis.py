# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:07:09 2020

@author: QCIT_ZQ
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
#import os


###################################
#函数名称：read_data
#函数功能：读取文件内的数据
#输入参数：file_name，文件路径
#作    者：臧强
#日    期：2020年8月6日14:59:35
#版    本：Ver1.0
###################################
def read_data(file_name):
    pressure_1 = []
    pressure_2 = []
    pressure_diff = []
    
    with open(file_name, 'r') as file_to_read: #打开文件
        while True:
            lines = file_to_read.readline()  #读取行数
            if not lines:
                break
                pass
            #将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符
            pressure_1_tmp, pressure_2_tmp, pressure_diff_tmp = [float(i) for i in lines.split()] 
            pressure_1.append(pressure_1_tmp)
            pressure_2.append(pressure_2_tmp)
            pressure_diff.append(pressure_diff_tmp)
            pass
        pressure_1 = np.array(pressure_1)
        pressure_2 = np.array(pressure_2)
        pressure_diff = np.array(pressure_diff)
        pass
    return pressure_1, pressure_2, pressure_diff


###################################
#函数名称：main
#函数功能：主函数
#输入参数：无
#作    者：臧强
#日    期：2020年8月6日17:06:27
#版    本：Ver1.0
###################################
def main():
    pressure_6, pressure_93, pressure_diff = read_data("plot/data/test.txt")
    data_len = len(pressure_6)
    
    #fig = plt.figure(figsize = (20,12))
    #plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示
    #plt.rcParams['axes.unicode_minus'] = False #解决符号无法显示
    #plt.scatter(pos_x_1,pos_y_1,label = '测试点1')
    #plt.scatter(13.119,5.656,label = '标定点1')
    #plt.plot(pos_x_run,pos_y_run)
    #plt.xlabel("x坐标/米")
    #plt.ylabel("y坐标/米")
    #plt.title("静态坐标测试")
    #plt.grid()
    #plt.xlim(4,16)
    #plt.ylim(0, 7.5)

    plt.plot(pressure_6)
    plt.show()
    
main()


