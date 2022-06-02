import random
import string

# Listado de Palabras que podran ser escogidas
palabras = ["enfermera", "farmacia", "vitaminas", "pastillas", "dentista", "ciego", "correr", "caminar", "regresar", "saltar", "fin", "cerrar", "nombre", "mujer", "hombre", "soltero", "novio", "nacer", "vivir", "edad", "anciana","trabajar", "cobrar", "azafata", "artista", "panadero", "carpintero", "cocinero", "maestro", "bombero", "juez", "modelo", "monje", "pintor", "piloto", "secretaria", "taxista", "escritor", "jefe", "aprendiz", "jubilado", "empleo", "industria", "taller", "tienda", "vacaciones", "sueldo", "impuesto", "huelga", "obedecer", "locura", "humor", "inteligencia", "suspirar", "preocupado", "risa", "amor", "suerte", "enamorado", "ver", "apagar", "luz", "color", "lupa", "microscopio", "claro", "cantar", "silbar", "voz", "eco", "trueno", "altavoz", "radio", "auricular", "liso", "comer", "dulce", "salado", "perfume", "despertarse", "vestirse", "desayunar", "leer", "dormirse", "toalla", "cobija", "almuerzo", "sopa", "agua", "leche", "jugo", "sal", "pimienta", "vinagre", "cortar", "hervir", "planchar", "aspiradora", "plancha", "horno", "abrelatas", "vajilla", "vaso", "cafetera", "azucarera", "comprar", "gastar", "vender", "barato", "caro", "gratis", "cliente", "bolsa", "cantar", "bailar", "libro", "revista", "clavo", "cine", "pala", "cocina", "hielo", "coro", "piano", "cartas", "pesca", "radio", "noticias", "televisor", "documental", "anuncio", "aplaudir", "teatro", "circo", "mago", "disco", "portero", "propina", "regalo", "comedor", "plaza", "calle", "estacionamiento", "parque", "puente", "puerto", "edificio", "escuela", "museo", "estatua", "fuente", "turista", "mendigo", "manejar", "acelerar", "frenar", "cruzar", "reparar", "conductor", "multa", "atasco", "carretera", "peaje", "curva", "florecer", "campo", "bosque", "huerto", "selva", "tronco", "rama", "flor", "hoja", "musgo", "cedro", "roble", "pino", "nogal", "naranjo", "tallo", "clavel", "margarita", "amapola", "rosa", "girasol", "violeta", "gato", "perro", "vaca", "pato", "oveja", "conejo", "pez", "oso", "jirafa", "saldar"]


def obtener_palabra(palabras):
    """ Obtiene una palabra aleatoria de la lista de palabras inicial """
    
    palabra = random.choice(palabras)
    
    return palabra.upper()


def ahorcado():
    """ Funcion Main del Juego """
    
    print("=======================================")
    print(" ¡Bienvenido al juego! ")
    print("=======================================")

    palabra = obtener_palabra(palabras) # Se obtiene palabra para iniciar
    letras_por_adivinar = set(palabra)  # Se pasa a conjunto la palabra con la que se va a jugar
    abecedario = set(string.ascii_uppercase) # Todas las letras del a abecedario
    letras_adivinadas = set()  # Letras que va asertando el usuario.

    vidas = int(input("Seleccione a cuantas vidas quiere jugar: ")) # Se establece el numero de vidas para el ahorcado

    # Mientras haya vidas y letras por adivinar se siguen escogiendo letras
    while len(letras_por_adivinar) > 0 and vidas > 0:
        # Muestra estado de vidas y letras
        print(f"Te quedan {vidas} vidas y has usado estas letras: {'-'.join(letras_adivinadas)}") # Join genera la cadena de caracteres a mostrar en forma de String separados por espacios en este caso

        # Estado actual del jugador
        palabra_lista = [] # Listado de las letras adivinadas hasta el momento
        for letra in palabra:
            if letra in letras_adivinadas:
                palabra_lista.append(letra)
            else:
                palabra_lista.append("-")
        print(f"Palabra: {' '.join(palabra_lista)}") # Muestra las letras separadas por espacio y con guiones en las letras que aun no se adivinaron

        # Usuario ingresa letra
        letra_elegida_por_usuario = input('Escoge una letra: ').upper()

        # Si la letra escogida por el usuario esta en el abecedario y no está en el conjunto de letras que ya se han ingresado, se añade la letra al conjunto de letras ingresadas.
        if letra_elegida_por_usuario in (abecedario - letras_adivinadas):
            letras_adivinadas.add(letra_elegida_por_usuario)
            # Si la letra está en la palabra, se elimina la letra del conjunto de letras que faltan adivinar. 
            if letra_elegida_por_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_elegida_por_usuario)
                print('')
            # Si la letra no está en la palabra, pierde una vida.
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_elegida_por_usuario} no está en la palabra.")
        # Si la letra escogida por el usuario ya fue ingresada se muestra error
        elif letra_elegida_por_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es válida.")

    # RESULTADO
    # Se sale del while cuando se queda sin vidas o se adivino la palabra se da resultado
    if vidas == 0:
        print(f"PERDISTE, La palabra era: {palabra}")
    else:
        print(f'GANASTE! La palabra era {palabra}!')

if __name__ == '__main__':
    ahorcado()