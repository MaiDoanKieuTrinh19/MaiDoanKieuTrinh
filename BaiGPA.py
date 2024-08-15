# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 08:16:43 2024

@author: MaiDoanKieuTrinh-23732851
"""
GPA=float(input('Nhập điểm trung bình GPA:'))
if GPA<3.5:
    print('Học lực kém')
elif GPA>=3.5 and GPA<5.0:
    print('Học lực yếu')   
elif GPA>=5.0 and GPA<7.0:
    print('Học lực trung bình')
elif GPA>=7.0 and GPA<8.0:
    print('Học lực khá')
elif GPA>=8.0 and GPA<9.0:
    print('Học lực giỏi')
elif GPA>=9.0 and GPA<=10.0:
    print('Học lực xuất sắc')
else:
    print('Không xác định')
    
