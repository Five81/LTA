# -*- coding: utf-8 -*-

import codecs

class DataFile:
    
    def __init__(self, path):
        self.f = codecs.open(path, 'w', 'utf-8')
        self.f.write("SoftwareName,Feature,isMalware\n")
    
    def append(self, name, feature, isMalware):
        self.f.write(
                "".join([name, ",", feature, ",", str(isMalware), "\n"])
                )
    
    def close(self):
        self.f.close()