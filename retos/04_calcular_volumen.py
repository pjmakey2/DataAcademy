"""
author: pjmakey2@gmail.com PJL
"""
import math
import argparse
parser = argparse.ArgumentParser(description='Calcular Geometrica Volumen')
figures = ['cilindro', 'cubo', 'ortoedro', 'cono', 'tronco_cono', 'esfera', 'tetraedro_regular']
parser.add_argument('--figura', dest='figura', nargs='?', choices=figures,help='Choice a figure please', required=True)
parser.add_argument('--lados', dest='lados', nargs='+', help='Sides of the figure',  type=float)
parser.add_argument('--altura', dest='altura', nargs='?', help='Higth of the figure',  type=float)
parser.add_argument('--radio', dest='radio', nargs='+', help='Radio of the figure', type=float)

args = parser.parse_args()
ff = args.figura
lados = args.lados
altura = args.altura
radio = args.radio

def calculate_vol(ff, lados, altura, radio):
    if ff in ['cilindro', 'cono']:
        if not altura or not radio: return 'Altura y radio son requeridos'
        if ff == 'cilindro': value = vol_cilindro(radio, altura)
        else: value = vol_cono(radio, altura)
    if ff in ['cubo', 'tetraedro_regular']:
        if not lados: return 'El lado es requerido'
        if ff == 'cubo': value = vol_cubo(lados)
        else: value = vol_tetraedro_regular(lados)
    if ff == 'ortoedro':
        if not lados: return 'El lado es requerido'
        if len(lados) < 3: return '3 lados son requeridos'
        value = vol_ortoedro(lados)
    if ff == 'tronco_cono':
        if not altura or not radio: return 'Altura y radio son requeridos'
        if len(radio) < 2: return 'Falta el radio superior'
        value = vol_tronco_cono(altura, radio)
    if ff == 'esfera':
        if not radio: return 'El radio es requeridos'
        value = vol_esfera(radio)
    return F'El Volumen de la figura {ff} = {value:,.4f}'
        

def vol_cilindro(radio, altura):
    return (math.pi*math.pow(radio[0], 2))*altura

def vol_cono(radio, altura):
    return ((math.pi*math.pow(radio[0], 2))*altura)/3

def vol_cubo(lados):
    return math.pow(lados[0], 3)

def vol_tetraedro_regular(lados):
    return (math.sqrt(2)*math.pow(lados[0], 3))/12

def vol_ortoedro(lados):
    return math.prod(lados[0:3])

def vol_tronco_cono(altura, radio):
    return (math.pi*(math.pow(radio[1], 2) + math.pow(radio[0], 2) + math.prod(radio)))/3

def vol_esfera(radio):
    return (4*math.pi*math.pow(radio[0], 3))/3

rsp = calculate_vol(ff, lados, altura, radio)
print(rsp)
