"""
author: pjmakey2@gmail.com PJL
"""
import argparse
parser = argparse.ArgumentParser(description='Conversor')
parser.add_argument('--tipo', dest='tipo', nargs='?', choices=['mil', 'km'],help='What you want to convert', required=True)
parser.add_argument('--value', dest='value', nargs='?', help='Value that you want to convert', required=True, type=float)
args = parser.parse_args()

tipo = args.tipo
value = args.value

def conversor(tipo, value):
    KMB = 1.609344
    cc = {
        'mil': lambda x: x*KMB,
        'km': lambda x: x/KMB
    }

    print(cc.get(tipo)(value))
    return cc.get(tipo)(value)

rsp = conversor(tipo, value)
ntipo = 'km' if tipo == 'mil' else 'mil'
print(F'Conversion: -> {value:,.2f}{tipo} = {rsp:,.2f}{ntipo}')
        

    
