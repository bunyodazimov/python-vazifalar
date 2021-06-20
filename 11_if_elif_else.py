# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 18:05:26 2021

@author: NITRO
"""

#1-amaliyot
'''
a=int(input('Juft son kriting: '))
if a%2==0:
    print('Rahmat')
else:
    print('Bu son juft emas')
'''  

#2-amaliyot
'''
yosh=int(input('Yoshingiz nechchida: '))
if yosh<=4 or yosh>=60:
    price=0
elif yosh<18:
    price=10000
else:
    price=20000
print(f"Chipta narxi {price} so'm")
'''

#3-amaliyot
'''
son1=float(input('1-sonni kiriting:>>> '))
son2=float(input('2-sonni kiriting:>>> '))
if son1==son2:
    price='='
elif son1>son2:
    price='>'
elif son1<son2:
    price='<'
print(f"{son1} {price} {son2}")
'''        

#4-amaliyot
'''
mahsulotlar=['anor','uzum','olma','o\'rik','banan','nok','tarvuz','sbzi','kartoshka','piyoz']
savat=[]
for n in range(5):
    savat.append(input(f"Savatga {n+1} - mahsulotni qo\'shing:>>> "))
if savat:
for mahsulot in savat:
        if mahsulot.lower() in mahsulotlar:
            print(f"{mahsulot.title()} mahsuloti do\'konimizda bor")
        else:
            print(f"{mahsulot.title()} mahsuloti do\'konimizda yo\'q")
else:
    print('Savatchangiz bo\'sh')
'''    
    
 #5-amaliyot
'''
mahsulotlar=['anor','uzum','olma','o\'rik','banan','nok','tarvuz','sabzi','kartoshka','piyoz']

bor_mahsulot=[]
mavjud_emas=[]
for n in range(5):
    mahsulot=(input(f"Savatga {n+1} - mahsulotni qo\'shing:>>> "))   
    if mahsulot in mahsulotlar:
        bor_mahsulot.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if mavjud_emas:
    print('Quyidagi mahsulotlar do\'konimizda yo\'q')
    for mahsulot in mavjud_emas:
        print(mahsulot) 
else:
    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
'''    
    
 #6-amaliyot
'''
foydalanuvchilar=['Jonibek','Jamol','Javoxir','Jaxongir','Jamshid']
login=input('Yangi login tanlang: ')
if login.title() in foydalanuvchilar:
    print('Login band, yangi login tanlang')
else:
    print(f"Xush kelibsiz, {login}!")
'''

#7-amaliyot
son=int(input('Istalgan butun son kiriting: '))
for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
    
    
    
    
    
    
    
    
    
    
    
    