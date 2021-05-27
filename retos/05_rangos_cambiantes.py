"""
author: pjmakey2@gmail.com PJL
"""
import math
import argparse

print("""
Bienvenido al programa RANGOS CAMBIANTES
-----------------------------------------

Por favor ingrese 3 numeros

El primer numero debe ser  el limite inferior

El segundo numero debe ser el limite superior

El tercer numero debe ser un numero de comparasion

""")

print('Primer Numero: ')
fn = input()
print('Segundo Numero: ')
sn = input()
print('Numero de comparasion: ')
cn = input()

try:
    fn, sn, cn = map(int, [fn, sn, cn])
except:
    raise Exception('Por favor en todos los casos ingrese numeros')

if fn > sn:
    raise Exception(F'El limite inferior {fn} es superior al superior {sn}')

def comparar(fn, sn, cn, newn=False):
    if newn:
        print(F'Ingrese un numero:')        
        cn = input()
        try:
            cn = int(cn)
        except:
            comparar(fn, sn, cn, newn=True)
        else:
            comparar(fn, sn, cn, newn=False)
    if cn >= fn and cn <= sn:
        return F'El numero de compracion = {cn} se encuentra entre el limite inferior {fn} y el superior {sn}'
    if cn < fn:
        print(F'El numero de compracion = {cn} se encuentra por debajo el limite inferior {fn}')
        comparar(fn, sn, cn, newn=True)
    if cn > sn:
        print(F'El numero de compracion = {cn} se encuentra por encima el limite superior {sn}')
        comparar(fn, sn, cn, newn=True)
    
rsp = comparar(fn, sn, cn)
print(rsp)


