# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 08:24:47 2024

@author: MaiDoanKieuTrinh-23732851
"""
print('Giải phương tình bậc nhất ax+b=0')
a=float(input('a='))
b=float(input('b='))
if a==0 and b==0:
    print('Phương trình vô số nghiệm')
elif a==0 and b!=0:
    print('Phương trình vô nghiệm')
elif a!=0:
    x=-b/a
    print('Phương trình có nghiệm x',x)
else:
    print('Không xác định')
    

