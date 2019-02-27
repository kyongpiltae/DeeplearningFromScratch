# coding: utf-8

#$$
#import import_ipynb
import sys, os
'''
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
'''
print('python : ',sys.executable)
print('project path:',os.getcwd())
print('directory path:', os.path.realpath('.'))
curpath = None
pardir =None

try:
    curpath = os.path.realpath(__file__) #"d:\code\deep-learning-from-scratch\ch03\mnist_show.py"
    curpath = os.path.dirname(curpath)
except NameError:
    print('NameError, it was excuted by command')
    curpath = os.path.realpath('.')

print('curpath: ',curpath)
pardir = os.path.dirname(curpath)
print('pardir: ', pardir)

# parent directory add.
sys.path.append(pardir)
#sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

os.chdir(curpath)
print('changed curpath:',os.getcwd())

import numpy as np
from dataset.mnist import load_mnist



from PIL import Image
#


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)


img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)  # (784,)
img = img.reshape(28, 28)  # 형상을 원래 이미지의 크기로 변형
print(img.shape)  # (28, 28)

img_show(img)
