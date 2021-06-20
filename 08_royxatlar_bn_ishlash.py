# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 23:07:30 2021

@author: NITRO
"""

#ro'yxatlar bilan ishlash
davlatlar=['amerika','angilya', 'fransiya','arabiston','xitoy','yaponya','shvetsarya','rassiya','ispanya']

print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)

davlatlar.reverse()
print(davlatlar)


davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)


j_sonlar=list(range(120,1200,2))
#print(j_sonlar)
jami=sum(j_sonlar)
arzon=min(j_sonlar)
qimmat=max(j_sonlar)
print(jami)
print(arzon-qimmat)
print(len(j_sonlar))
#boshidan 20 ta
print(j_sonlar[:20])
#o'rtasidan 20 ta
print(j_sonlar[-20:])
#oxiridan 20 ta
print(j_sonlar[520:540])

taomlar=['mastava','shorva','osh','lagmon','norin']
nonushta=taomlar[:]
nonushta.remove('osh')
nonushta.remove('lagmon')
nonushta.remove('norin')
nonushta.append('smetana')
nonushta.append('sut')
print(taomlar)
print(nonushta)
nonushta=('mastava','shorva','osh','lagmon','norin')
nonushta=list(nonushta)
nonushta[0]='qaymoq'
print(nonushta)

