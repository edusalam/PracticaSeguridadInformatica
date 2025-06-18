#estructura de control
'''
eduard = 10

if eduard ==67:
    print('el valor es verdadero')
if eduard == 10:
    print('el valar es 10')

eduard = 10
if eduard % 2 == 0:
    print('el resto es cero')

else: 
    print('el resto no es cero')

lista = [1,2,3,4,5,6]
indice = 0
while indice < len(lista):
    print(lista[indice])
    indice +=1

diccionario = {'eduard':'amaya','estudiantes':'genios'}
type(diccionario)
#diccionario['eduard']

apilar = [1,2,3,4]
apilar.append(5)
apilar

from collections import deque
colas = deque()
colas

ingreso = input('ingrese tu clase')

#salida por panntalla
print('hola')
'''
def atras(segundos):
    segundos -= 1
    if segundos >=  0:
        print(segundos)
        atras(segundos)
    else:
        print('termino la cuenta atras')
        



