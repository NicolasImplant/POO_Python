from Borracho import BorrachoTradicional , Borracho
from campo import Campo
from coordenada import Coordenada

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(Borracho)
    for _ in range(pasos):
        campo.mover_borracho(Borracho)
    return inicio.distancia(campo.obtener_coordenada(Borracho))

def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    Borracho = tipo_de_borracho(nombre = 'David')
    origen = Coordenada(0,0)
    distancias = []
    return distancias
    
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.añadir_borracho(Borracho, origen)
        simular_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simular_caminata,1))

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias)/len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} Caminara aleatoria de {pasos} ')
        print(f'media = {distancia_media}')
        print(f'maxima = {distancia_maxima}')
        print(f'minima = {distancia_minima}')

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 100

    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)

