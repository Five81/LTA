# -*- coding: utf-8 -*-
import os
from infrastructure.ware import Ware
from infrastructure.fileutils import DataFile

# virusroot = "malware"
kindroot = "n-gram\\kind"

# 打开文件以写入特征数据
f = DataFile("\\n-gram\\data1.csv")


def collect(rootdir, isMalware):
    wares = os.listdir(rootdir)
    total = len(wares)
    for i, ware in enumerate(wares):
        warePath = os.path.join(rootdir, ware)
        try:
            ware = Ware(warePath, isMalware)
            ware.extractFeature(f)
            print("已提取", i + 1, "个文件的特征，百分比如下：")
            print((i + 1) * 100 / total, "%")
        except Exception as e:
            print("在处理文件", warePath, "时发生错误:", str(e))
            print("跳过该文件，继续下一个文件")
            continue

    # 在处理完当前目录的所有文件后，关闭文件
    f.close()


# 1代表恶意软件
# collect(virusroot, 1)
collect(kindroot, 0)
        




