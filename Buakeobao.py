# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:42:44 2024

@author: MaiDoanKieuTrinh-23732851
"""
print('Game kéo búa bao nè!')
from random import randint 
Nguoi=int(input('Bạn vui lòng chọn: 1. Kéo, 2. Búa, 3. Bao: '))
May=randint(1,3)
if May==1:
    print('Máy chọn Kéo')
elif May==2:
    print('Máy chọn Búa')
elif May==3:
    print('Máy chọn Bao')
if May==Nguoi:
    print('HÒA')
if May==1 and Nguoi==2:
    print('BẠN THẮNG') 
if May==1 and Nguoi==3:
    print('MÁY THẮNG')
if May==2 and Nguoi==1:
    print('MÁY THẮNG')
if May==2 and Nguoi==3:
    print('BẠN THẮNG')
if May==3 and Nguoi==1:
    print('BẠN THẮNG')
if May==3 and Nguoi==2:
    print('MÁY THẮNG')