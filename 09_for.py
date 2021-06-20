# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 09:06:10 2021

@author: NITRO
"""
#1-amaliyot
ismlar=['jonibek','jamol','sanjar','javoxir','muslim']
for ism in ismlar:
    print(f"Salom {ism}")
print(f"kod {len(ismlar)} marta takrorlandi")

#2-amaliyot
sonlar=list(range(11,100,2))
for kubi in sonlar:
    print(f"{kubi} sonining kubi: {kubi**3}")

#3-amaliyot
kinolar=[]
#for n in range(5):
   # kinolar.append(input(f"{n+1}-yoqtirgan kinoyingiz: "))
#print(kinolar)

#4-amaliyot
n_people=int(input('bugun nechta odam bn suhbat qildingiz:>>> '))
suhbatdoshlar=[]
for n in range(n_people):
    suhbatdoshlar.append(input(f"{n+1}-suhbatdoshingiz kim: "))
print(suhbatdoshlar)