#author:九世
#time:2019/2/16

import os

def pd(files):
    if os.path.exists(files):
        return 1
    else:
        return 0