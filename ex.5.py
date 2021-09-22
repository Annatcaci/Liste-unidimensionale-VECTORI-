import abc


x=[1,2,3,4,5]
y=x
#a)
suma=0
for element in range(0,3):
    suma=suma+x[element]
print("Suma primelor 3 componente: ",suma)
#b)
print("Suma tuturor componentelor variabilei y: ",sum(y))
#c)
produs=1
for element in range(0,len(x)):
    produs=produs*x[element]
print("Produsul tuturor componentelor variabilei x: ",produs)
#d)
z=y[2]
print("Valoarea absoluta a componentului 3 din sirul y: ",abs(z))
#e)
print("Suma primelor comonente a listelor x si y: ",x[0]+y[0])

