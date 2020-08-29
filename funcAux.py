from sys import argv
from os import path, mkdir
from re import search

def minihelp():
    print("USO: python3 calculator.py <ARCHIVO> \"<DELIMITADOR>\"")
    print("Argumento \"--help\" para mostrar más información")
    exit()

def fullhelp():
    print("\n USO: python3 calculator.py <ARCHIVO> \"<DELIMITADOR>\"")
    print(" 2º Argumento: Archivo con datos")
    print(" 3º Argumento: Delimitador del fichero")
    print(" Delimitadores inválidos son: '-'\n")
    print(" Ejemplo entrada con delimitador (;):\t13-05-2013;M;56.4;163;20;44.5;7.2;60;72.4;45.1;13;6.6")
    print("""
 Datos de la entrada por orden:
    - Fecha (Día-Mes-Año)
    - Sexo (M/H)
    - Peso (Kg.)
    - Altura (cm.)
    - Edad
    - Perímetro del pecho (cm.)
    - Perímetro del brazo (cm.) 
    - Perímetro del cintura (cm.)
    - Perímetro de la cadera (cm.)
    - Perímetro del muslo (cm.)
    - Perímetro del gemelo (cm.)
    - Perímetro del tobillo (cm.)
    """)
    print(" El fichero puede almacenar entradas para diferentes días.")
    print(" Teniendo esto en cuenta, se calculará la diferencia en términos de pérdidas/ganancias respecto a la fecha anterior.")
    exit()

def comprobarArgumentos():

    if (len(argv) == 2):
        if (argv[1] == "--help"):
            fullhelp()
        else:
            minihelp()
    elif (len(argv) != 3):
        minihelp()

    archivo = argv[1]
    delim = argv[2]

    if (delim == "-"):
        print("No se acepta \"-\" como delimitador.")
        minihelp()

    if (path.exists(archivo) is False):
        print("El archivo \"" + archivo + "\" no existe.")
        exit()
    
    # Crea carpeta para las gráficas
    if not path.exists("output"):
        mkdir("output")
    else:
        if not path.isdir("output"):
            mkdir("output")

    return archivo, delim

def verificarLinea(linea):
    valores = ["Fecha", "Sexo", "Peso", "Altura", "Edad", "Perímetro de pecho", "Perímetro de brazo", "Perímetro de cintura", "Perímetro de cadera", "Perímetro de muslo", "Perímetro de gemelo", "Perímetro de tobillo"]
    # Fecha
    if((search(r'(\d+-\d+-\d+)',linea[0])) is None):
        print("¡ERROR!\nComprueba la línea con \"" + valores[0] + "\": " + linea[0])
        return 1
    # Sexo
    if (linea[1] != "M" and linea[1] != "H"):
        print("¡ERROR!\nComprueba la línea con \"" + valores[1] + "\": " + linea[1])
        return 1
    # Demás valores
    for i in range(2,len(linea)-1):
        if((search(r'(\d+(?:\.\d+)?)',linea[i])) is None):
            print("¡ERROR!\nComprueba la línea con \"" + valores[i] + "\": " + linea[i])
            return 1

def floatify(texto):
    return round(float(texto),2)

def diferencia(num1,num2,tolerancia):
    if (num1 > num2):
        if (num1 - num2 <= tolerancia):
            return 0
        else:
            return 1
    else:
        if (num2 - num1 <= tolerancia):
            return 0
        else:
            return 1

class Datos():
    def __init__(self, fecha, sexo, peso, altura, edad, pecho, brazo, cintura, cadera, muslo, gemelo, tobillo):
        self.fecha = fecha
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.edad = edad
        self.pecho = pecho
        self.brazo = brazo
        self.cintura = cintura
        self.cadera = cadera
        self.muslo = muslo
        self.gemelo = gemelo
        self.tobillo = tobillo