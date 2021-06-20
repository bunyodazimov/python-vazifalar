# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:02:05 2021

@author: NITRO
"""

ismlar= ["Nuriddin","Mirxomid","Dilshod"]
print("Salom "+ismlar[0]+" bugun choyxona bormi?")
print(ismlar[1]+" choyxonaga baramizmi?")

#Sonlar ustida amallar
sonlar=[12,-5,10.5,0.5]
sonlar[1]=sonlar[2]+5
sonlar.append(21)
sonlar.insert(1, 22)
del sonlar[0]


mevalar=["olma", "banan", "gilos","o'rik"]
mahsulot=mevalar.pop(2)
print("Men "+mahsulot+" sotib oldim")
print("Olinmagan mahsulotlar ", mevalar)


t_shaxslar=['Imom Buxoriy','Bobur','Amir Temur', 'Alisher Navoiy']
z_shaxslar=['Bill Gates','Sariq Dev','Alisher Usmonov', 'Ronaldo']
t_shaxs=t_shaxslar.pop(0)
z_shaxs=z_shaxslar.pop(1)
print("Men tarixiy shaxslardan "+t_shaxs+" bilan suhbat qurishni istardim"+
      '\nZamonaviy shaxslardan esa '+z_shaxs+'bilan suhbat qilishni istardim')

friends=[]
friends.append('Nuriddin')
friends.append('Muslim')
friends.append('Jamol')
friends.append('Jonibek')
friends.append('Javoxir')
friends.remove('Nuriddin')
friends.remove('Muslim')
friends.insert(0,'Ibrohim')
friends.insert(-1,'Sarvar')
friends.insert(5, 'Jaxongir')
mehmonlar=[]
kelgan1=friends.pop(0)
kelgan2=friends.pop(2)
mehmonlar.append(kelgan1)
mehmonlar.append(kelgan2)
print(friends)
print(mehmonlar)