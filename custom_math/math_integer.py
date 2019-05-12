from helper_function import read_lines_from_folder

def add2number(a,b,threshold):
    return threshold if (a+b)>threshold else a+b
def product2number(a,b,threshold):
    return threshold if (a*b)>threshold else a*b