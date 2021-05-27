"""
author: pjmakey2@gmail.com PJL
"""
import argparse
parser = argparse.ArgumentParser(description='Triangulos')
parser.add_argument('--base', dest='base', nargs='?',help='Base of the triangulo', required=True, type=int)
parser.add_argument('--altura', dest='altura', nargs='?',help='Higth of the triangulo', required=True, type=int)
parser.add_argument('--lados', dest='lados', nargs=3,help='Triangles sides', required=True, type=int)
args = parser.parse_args()

def calcular_area(*args):
    base, altura = args
    return (base*altura)/2

def tipo_triangulo(*args):
    l1, l2, l3 = args
    if l1 == l2 == l3: return 'Triangulo Equilatero'
    if (l1 == l2) or (l1 == l3) or (l2 == l3): return 'Triangulo Isoceles'
    if l1 != l2 != l3: return 'Triangulo Escaleno'

base = args.base
altura = args.altura

rsp_ca = calcular_area(base, altura)
rsp_tt = tipo_triangulo(*args.lados)

print(F'La base del triangulo es {base}')
print(F'El tipo de triangulo es {rsp_tt}')

