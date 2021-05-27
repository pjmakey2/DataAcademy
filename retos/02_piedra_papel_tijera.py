"""
author = pjmakey2@gmail.com PJL
"""
from pprint import pprint
import getpass
opts = {
    1: 'Piedra',
    2: 'Papel',    
    3: 'Tijera',
}
print("""
####NOTA: Al escribir la opcion no se observa lo escrito, para que sea mas justo el juego
Numero de jugadores: 2
El jugador numero 1 ingresa una opcion 
El jugador numero 2 ingresa una opcion 
El sistema determina el ganador
\n
LISTA DE OPCIONES:--->
""")
pprint(opts, width=5)
print('#####################')
print('\nComienza el juego!!!!')
usera = getpass.getpass('Usuario 1, ingrese una de las opciones: ')
userb = getpass.getpass('Usuario 2, ingrese una de las opciones: ')


def hands_game(*args):
    usera, userb = args
    try:
        int(usera)
        int(userb)
    except:
        return 'Las opciones deben ser numeros'
    usera, userb = map(int, [usera, userb])    
    useraoa = opts.get(usera)
    useraob = opts.get(userb)
    if useraoa == None or useraob == None: return 'Opcion invalida'
    ganador = ''
    if usera == userb:
        ganador = F'Es un empate {useraoa} == {useraob}'
    if usera == 1 and userb == 2:
        ganador = F'El ganador es el usuario 2 {useraob} > {useraoa}'
    if usera == 1 and userb == 3:
        ganador = F'El ganador es el usuario 1 {useraoa} > {useraob}'        
    if usera == 2 and userb == 3:
        ganador = F'El ganador es el usuario 2 {useraob} > {useraoa}'
    if userb == 1 and usera == 2:
        ganador = F'El ganador es el usuario 1 {useraoa} > {useraob}'
    if userb == 1 and usera == 3:
        ganador = F'El ganador es el usuario 2 {useraob} > {useraoa}'        
    if userb == 2 and usera == 3:
        ganador = F'El ganador es el usuario 1 {useraoa} > {useraob}'                        
    return ganador
print('\n')
rsp = hands_game(usera, userb)
print(rsp)
print('\nFin del juego')
