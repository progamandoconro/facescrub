#conda activate my_env
#cd Downloads/download
#######################################################
import os
from PIL import Image
import glob
from matplotlib import image

ob = os.popen('find . -name "*.jpg"') #encuetra todos los jpg en dir y subdirs en wd
dir_fotos = list(ob)
dir_fotos = [x[:-1] for x in dir_fotos]



list=[]
for i in dir_fotos:
    list[i] = str.split(i,"/")[-1]
