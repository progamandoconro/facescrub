#conda create -n my_env python=3.7
#conda activate my_env
#cd Downloads/download
#python
#######################################################
import os
from PIL import Image
import glob
from matplotlib import image
import shutil

ob = os.popen('find . -name "*.jpg"') #encuetra todos los jpg en dir y subdirs en wd
dir_fotos = list(ob)
dir_fotos = [x[:-1] for x in dir_fotos]
list=[]
for i in dir_fotos:
    new = str.split(i,"/")[-1]
    list.append(new)

src_dir = "home/ro/Downloads/download"
dst_dir = "home/ro/Downloads/download"
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    shutil.copy(jpgfile, dst_dir)

#find . -name '*' -exec file {} \; | grep -o -P '^.+: \w+ image' | cut -d':' -f1 | xargs -I{} cp -v {} /home/joachim/neu2

list2=[]
for i in new:
    new2 = image.imread(new)
    list2.append(new2)

####################################################################
