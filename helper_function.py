"""
 Read text by line from a folder
 Input:
        Path to folder
 Output:
        Numpy array of line of all text of all file in folder
"""

import numpy as np
import pandas as pd
import os
def read_lines_from_folder(path):
    all_file = os.listdir(path)
    print(all_file)
    content = []
    for each_file in all_file:
        if each_file.endswith(".txt"):
            file_path = os.path.join('', *[path,each_file])
            print(file_path)
            fileobj = open(file_path,'r')
            for each_line in fileobj:
                content.append(each_line)
            fileobj.close()
    content = np.array(content)
    return content


