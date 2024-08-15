# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:13:49 2024

@author: MaiDoanKieuTrinh-23732851
"""
print('Tiền taxi')
s=float(input('Nhập số km quãng đường:'))
if s==1:
    sotien=20000 
elif s<=3:
    sotien=20000+2*13000
elif s>=4 and s<=8:
    sotien=20000 + 2*13000 +(s-3)*12000
elif s>8:
    sotien=20000+ 2*13000+ 5*12000+(s-8)*10000
if sotien>100:
    tongsotien=sotien*(92/100)
else:
    tongsotien= sotien 
print('Số tiền taxi là:', tongsotien)
