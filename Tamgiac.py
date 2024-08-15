# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 08:53:47 2024

@author: MaiDoanKieuTrinh-23732851
"""
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a+b>c and b+c>a and a+c>b:
    if a==b and b==c:
        print('{}, {}, {}, là 3 cạnh của tam giác đều'.format(a,b,c))
    elif a==b or  a==c or b==c:
        print('{}, {}, {}, là 3 cạnh của tam giác cân'.format(a,b,c))
    elif a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2:
        print('{}, {}, {}, là 3 cạnh của tam giác vuông'.format(a,b,c))
    else:
        print('{}, {}, {}, là 3 cạnh của tam giác'.format(a,b,c))
else:
    print('{}, {}, {}, không phải là 3 cạnh của tam giác'.format(a,b,c))