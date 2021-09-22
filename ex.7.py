venit=[200,53,8009,4567,678,83,245]
#a)
print("Venitul saptamanal: ",sum(venit))
#b)
print("Venitul zilnic mediu: ",sum(venit)//7)
#c)
a=venit.index(max(venit))
if a==0:
    print("Cel mai mult compania a primit luni")
elif a==1:
    print("Cel mai mult compania a primit marti")
elif a==2:
    print("Cel mai mult compania a primit miercuri")
elif a==3:
    print("Cel mai mult compania a primit joi")
elif a==4:
    print("Cel mai mult compania a primit vineri")
elif a==5:
    print("Cel mai mult compania a primit sambata")
elif a==6:
    print("Cel mai mult compania a primit duminica")
#d)
b=venit.index(min(venit))
if b==0:
    print("Cel mai putin compania a primit luni")
elif b==1:
    print("Cel mai putin compania a primit marti")
elif b==2:
    print("Cel mai putin compania a primit miercuri")
elif b==3:
    print("Cel mai putin compania a primit joi")
elif b==4:
    print("Cel mai putin compania a primit vineri")
elif b==5:
    print("Cel mai putin compania a primit sambata")
elif b==6:
    print("Cel mai putin compania a primit duminica")
