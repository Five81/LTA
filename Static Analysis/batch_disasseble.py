# -*- coding: utf-8 -*-


import os
import subprocess

def disassemble(frompath, topath, num, start=0):
    files = os.listdir(frompath)
    files = files[start:num]
        
    total = len(files)
    
    for i, file in enumerate(files):
        fullFrompath = os.path.join(frompath, file)
        fullTopath = os.path.join(topath, file)
        command = "apktool d " + fullFrompath + " -o " + fullTopath
        subprocess.call(command, shell=True)
        print("已反汇编", i, "个应用，百分比如下：")
        print((i + 1) * 100 / total, "%")


#反汇编恶意软件样本
# virus_root = "..\\bit\\virus\\VirusAndroid"
# virus_root =".\\Adware"
# disassemble(virus_root, ".\\smalis\\malware", 95)


#反汇编正常软件样本
kind_root = ".\\Benign"
disassemble(kind_root, ".\\smalis\\kind", 600)