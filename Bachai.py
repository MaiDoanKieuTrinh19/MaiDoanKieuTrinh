# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 08:30:04 2024

@author: MaiDoanKieuTrinh-23732851
"""
print('Giải phương tình bậc  ax^2+bx+c=0')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a==0:
    print('Phương trình không phải phương trình bậc hai')
elif a!=0:
    delta = b**2- 4*a*c
    if delta<0:
        print('Phương trình vô nghiệm')
    elif delta==0:
        x=-b/(2*a)
        print('Phương trình có nghiệm kép x=x1=x2=',x)
    elif delta>0:
        x1 = (-b+delta**(1/2))/(2*a)
        x2 = (-b-delta**(1/2))/(2*a)
        print('Phương trình có 2 nghiệm')
        print('x1=',x1)
        print('x2=',x2)
else:
    print('Không xác định')
    
        