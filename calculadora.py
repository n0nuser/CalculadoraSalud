#!/usr/bin/python3
from funcAux import comprobarArgumentos, Datos, verificarLinea, floatify
from funcIndices import ICC, ICA, RFM, IAC, IC, Agua, diffDatos, plots, imprimirDatos
from markdown import markdown
from bs4 import BeautifulSoup
import webbrowser


## COMPROBACIONES ARGUMENTOS

archivo,delim = comprobarArgumentos()

f = open(archivo,"r")
lines = f.readlines()
data = []
try:
    for i in range(len(lines)):
        linea = lines[i].split(delim)
        if(len(linea) != 12):
            print("¡ERROR!\nLa línea " + str(i) + " no contiene los doce elementos requeridos.")
            exit()
        linea[11] = linea[11][:-1] # Remove the break line
        if(verificarLinea(linea)):
            exit()
        data.append(Datos(linea[0],linea[1],floatify(linea[2]),floatify(linea[3]),int(linea[4]),floatify(linea[5]),floatify(linea[6]),floatify(linea[7]),floatify(linea[8]),floatify(linea[9]),floatify(linea[10]),floatify(linea[11])))
except:
    exit()

actual = data[-1]

# Crear el HTML a partir de Markdown

f = open('output/resumen.html', 'w')

texto = ""

html = "<!DOCTYPE html>\n<html>\n<head>\n<title>Resumen Salud</title>\n"
html = html + "<link rel=\"stylesheet\" href=\"../avenir-white.css\">\n"
html = html + "</head>\n<body>\n"

texto = texto + "# VALORES ACTUALES"
texto = texto + imprimirDatos(actual)

texto = texto + "\n# CÁLCULO ÍNDICES (ACTUAL)"
texto = texto + ICC(actual)
texto = texto + IC(actual)
texto = texto + ICA(actual)
texto = texto + RFM(actual)
texto = texto + IAC(actual)
texto = texto + Agua(actual)

if (len(lines) >= 2):
    texto = texto + "\n# DIFERENCIA DE LOS DATOS ACTUALES VS LOS ANTERIORES"
    textoPreTabla = texto

    htmlTabla = markdown(diffDatos(data[-1],data[-2]),extensions=['tables'])

    textoPosTabla = "\n# GRÁFICAS DATOS SEGÚN"
    textoPosTabla = textoPosTabla + plots(data)

html = html + markdown(textoPreTabla) + htmlTabla + markdown(textoPosTabla) + "</body>"
www = BeautifulSoup(html, 'html.parser')
www = www.prettify()

f.write(www)
f.close

webbrowser.get("firefox").open("output/resumen.html")
