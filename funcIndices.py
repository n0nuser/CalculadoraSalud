from funcAux import diferencia, Datos
from math import sqrt
from tabulate import tabulate
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates

# Markdown

h2 = "\n## "
h3 = "\n\n### "
def bold(texto):
    return("**" + texto +  "**")
def italic(texto):
    return("*" + texto +  "*")
def codeblock(texto):
    return("```\n" + texto +  "\n```")
def cita(texto):
    return("> " + texto)
def imagen(texto, imagen):
    return("\n![" + texto +  "](" + imagen + ")")
def link(texto,url):
    return("\n[" + texto +  "](" + url + ")")

# Variables Cambiables

intervaloDiasMuestra = 7 # Intervalo para las muestras de las Gráficas
tolerancia = 1 # Tolerancia para diferencia en índices

def imprimirDatos(clase):
    texto = ""
    texto = texto + "\n- Fecha: " + bold(clase.fecha)
    if(clase.sexo == "M"):
        texto = texto + "\n- Sexo: **Mujer**"
    else:
        texto = texto + "\n- Sexo: **Hombre**"
    texto = texto + "\n- Edad: " + bold(str(clase.edad) + " años")
    texto = texto + "\n- Peso: " + bold(str(clase.peso) + " kg.")
    texto = texto + "\n- Altura: " + bold(str(clase.altura) + " cm.")
    texto = texto + "\n- Perímetro del pecho: " + bold(str(clase.pecho) + " cm.")
    texto = texto + "\n- Perímetro del brazo: " + bold(str(clase.brazo) + " cm.")
    texto = texto + "\n- Perímetro del cintura: " + bold(str(clase.cintura) + " cm.")
    texto = texto + "\n- Perímetro de la cadera: " + bold(str(clase.cadera) + " cm.")
    texto = texto + "\n- Perímetro del muslo: " + bold(str(clase.muslo) + " cm.")
    texto = texto + "\n- Perímetro del gemelo: " + bold(str(clase.gemelo) + " cm.")
    texto = texto + "\n- Perímetro del tobillo: " + bold(str(clase.tobillo) + " cm.")

    return texto

def ICC(clase):
    # Índice Cintura Cadera: Normal hasta 0.90(H), 0.85(M).
    ## Perímetro Cintura / Perímetro Cadera
    # https://en.wikipedia.org/wiki/Waist%E2%80%93hip_ratio

    texto = ""
    icc = clase.cintura/clase.cadera
    icc = round(icc, 2)
    texto = texto + h2 + "Índice Cintura Cadera: " + bold(str(icc))
    texto = texto + h3 + "Descripción:"
    texto = texto + "\n\nEl ICC se ha usado como indicador o medición de la salud, y el riesgo de contraer enfermedades de salud serias."
    texto = texto + "\n\nTambién se relaciona con la fertilidad (con diferentes valores óptimos para hombres y mujeres):"
    texto = texto + "\n\n- Las mujeres con un rango cercano al 0.7 se encuentran en niveles óptimos de estrógenos (son por lo general más fértiles)."
    texto = texto + "\n  - Son menos susceptibles de contraer enfermedades como la diabetes, trastornos cardiovasculares o cáncer de ovarios."
    texto = texto + "\n- Los hombres con un ICC cercano al 0.9 han demostrado ser más saludables y fértiles con menos cáncer de próstata y testicular."
    texto = texto + h3 + "Resultado:"
    if(clase.sexo == "M"):
        rango = [x / 100.0 for x in range(71, 84)]
        if(icc in rango):
            texto = texto + "\n\nEl resultado es **normal** ya que está entre el 0.71 y el 0.84 estimado como normal para mujeres."
        else:
            texto = texto + "\n\nEl resultado es **anormal** ya que no está entre el 0.71 y el 0.84 estimado como normal para mujeres."
            texto = texto + "\n\nEstá asociado a un aumento en la probabilidad de contraer diversas enfermedades (diabetes mellitus, enfermedades coronarias, tensión arterial, entre otras)."
            if(icc < 71):
                texto = texto + "\n\nPosees síndrome ginecoide (cuerpo de pera)."
            else:
                texto = texto + "\n\nPosees síndrome androide (cuerpo de manzana)."
    else:
        rango = [x / 100.0 for x in range(78, 94)]
        if(icc in rango):
            texto = texto + "\n\nEl resultado es **normal** ya que está entre el 0.78 y el 0.94 estimado como normal para hombres."
        else:
            texto = texto + "\n\nEl resultado es **anormal** ya que no está entre el 0.78 y el 0.94 estimado como normal para hombres."
            texto = texto + "\n\nEstá asociado a un aumento en la probabilidad de contraer diversas enfermedades (diabetes mellitus, enfermedades coronarias, tensión arterial, entre otras)."
            if(icc < 78):
                texto = texto + "\n\nPosees síndrome ginecoide (cuerpo de pera)."
            else:
                texto = texto + "\n\nPosees síndrome androide (cuerpo de manzana)."

    return texto

def ICA(clase):
    # Índice Cintura Altura: Normal 0.35-0.5
    ## Perímetro cintura (cm.) / Altura (cm.)
    ## Si más de 0.5 riesgos típicos de obesidad: elevación triglicéridos, colesterol y glucosa en sangre, e hipertensión arterial
    # Análisis resultados: https://es.wikipedia.org/wiki/%C3%8Dndice_cintura/cadera

    texto = ""
    def extrDelgado(): return ("\n\nCategoría: **Extremadamente delgado**.\n\nEjemplo: Marilyn Monroe (0.3359)")
    def delgado(): return ("\n\nCategoría: **Delgado Sano**.\n\nEjemplo: Beyonce (0.3881) ó Kate Moss (0.3882)")
    def sano(): return ("\n\nCategoría: **Sano**.\n\nEjemplo: Nadador universitario (0.4260) ó un musculista (0.4580)")
    def sobrepeso(): return ("\n\nCategoría: **Sobrepeso**.\n\nRiesgo cardiovascular")
    def sobrepesoElevado(): return ("\n\nCategoría: **Sobrepeso Elevado**.\n\nRiesgo cardiovascular elevado")
    def sobrepesoMorbido(): return ("\n\nCategoría: **Sobrepeso Mórbido**.\n\nRiesgo cardiovascular muy elevado")

    ica = clase.cintura/clase.altura
    ica = round(ica, 2)
    texto = texto + h2 + "Índice Cintura Altura: " +  bold(str(ica))
    texto = texto + h3 + "Descripción:"
    texto = texto + "\n\nEl ICA es una medida de la distribución de la grasa corporal."
    texto = texto + "\n\nValores más altos del ICA indican mayor riesgo de obesidad relacionado con enfermedades cardiovasculares correlacionadas con la obesidad abdominal."
    texto = texto + "\n\nEs más preciso que el índice de masa corporal (IMC) tradicional."
    texto = texto + h3 + "Resultado:"
    if(clase.edad <= 15):
        if(ica < 0.34):
            texto = texto + extrDelgado()
        elif(ica >= 0.34 and ica < 0.45):
            texto = texto + delgado()
        elif(ica >= 0.45 and ica < 0.51):
            texto = texto + sano()
        elif(ica >= 0.51 and ica < 0.63):
            texto = texto + sobrepeso()
        else:
            texto = texto + sobrepesoElevado()
    elif(clase.edad > 15):
        if(clase.sexo == "M"):
            if(ica < 0.34):
                texto = texto + extrDelgado()
            elif(ica >= 0.34 and ica < 0.41):
                texto = texto + delgado()
            elif(ica >= 0.41 and ica < 0.48):
                texto = texto + sano()
            elif(ica >= 0.48 and ica < 0.53):
                texto = texto + sobrepeso()
            elif(ica >= 0.53 and ica < 0.57):
                texto = texto + sobrepesoElevado()
            else:
                texto = texto + sobrepesoMorbido()
        else:
            if(ica < 0.34):
                texto = texto + extrDelgado()
            elif(ica >= 0.34 and ica < 0.42):
                texto = texto + delgado()
            elif(ica >= 0.42 and ica < 0.52):
                texto = texto + sano()
            elif(ica >= 0.52 and ica < 0.57):
                texto = texto + sobrepeso()
            elif(ica >= 0.57 and ica < 0.62):
                texto = texto + sobrepesoElevado()
            else:
                texto = texto + sobrepesoMorbido()

    return texto

def RFM(clase):
    # Índice de Masa Grasa Relativa: Resultados similares a prueba DEXA
    ## Hombres: RFM = 64 - 20 * (altura (m.) / perímetro cintura (m.))
    ## Mujer: RFM = 76 - 20 * (altura (m.) / perímetro cintura (m.))
    # Análisis resultados: https://www.dexafit.com/blog2/what-is-the-ideal-body-fat-percentage

    texto = ""

    def bajo(): return ("\n\nNivel de grasa: **Bajo en grasa**")
    def saludable(): return ("\n\nNivel de grasa: **Saludable**")
    def sobrepeso(): return ("\n\nNivel de grasa: **Sobrepeso**")
    def obesidad(): return ("\n\nNivel de grasa: **Obesidad**")
    def noEdadRango(): return ("\n\nLas edades aceptadas para el cálculo son desde los 20 hasta los 79 años.")

    if(clase.sexo == "M"):
        rfm = 76 - 20 * ((clase.altura/100) / (clase.cintura/100))
        rfm = round(rfm,2)
        texto = texto + h2 + "Índice de Masa Grasa Relativa: " + bold(str(rfm))
        texto = texto + h3 + "Descripción:"
        texto = texto + "\n\nEl RFM arroja resultados similares a la prueba radiológica DEXA por lo que es muy precisa."
        texto = texto + "\n\nEs un procedimiento simple más conveniente que el porcentaje de grasa corporal y más preciso que el índice de masa corporal (IMC) tradicional."
        texto = texto + h3 + "Resultado:"
        if (clase.edad in range(20,40)):
            if (rfm < 21):
                texto = texto + bajo()
            elif(rfm >= 21 and rfm < 33):
                texto = texto + saludable()
            elif(rfm >= 33 and rfm < 39):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(40,60)):
            if (rfm < 23):
                texto = texto + bajo()
            elif(rfm >= 23 and rfm < 35):
                texto = texto + saludable()
            elif(rfm >= 35 and rfm < 40):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(60,80)):
            if (rfm < 24):
                texto = texto + bajo()
            elif(rfm >= 24 and rfm < 36):
                texto = texto + saludable()
            elif(rfm >= 36 and rfm < 42):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        else:
            texto = texto + noEdadRango()
    else:
        rfm = 64 - 20 * ((clase.altura/100) / (clase.cintura/100))
        rfm = round(rfm,2)
        texto = texto + h2 + "Índice de Masa Grasa Relativa: " + bold(str(rfm))
        texto = texto + h3 + "Descripción:"
        texto = texto + "\n\nEl RFM arroja resultados similares a la prueba radiológica DEXA por lo que es muy precisa."
        texto = texto + "\n\nEs un procedimiento simple más conveniente que el porcentaje de grasa corporal y más preciso que el índice de masa corporal (IMC) tradicional."
        texto = texto + h3 + "Resultado:"
        if (clase.edad in range(20,40)):
            if (rfm < 8):
                texto = texto + bajo()
            elif(rfm >= 8 and rfm < 19):
                texto = texto + saludable()
            elif(rfm >= 19 and rfm < 25):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(40,60)):
            if (rfm < 11):
                texto = texto + bajo()
            elif(rfm >= 11 and rfm < 22):
                texto = texto + saludable()
            elif(rfm >= 22 and rfm < 27):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(60,80)):
            if (rfm < 13):
                texto = texto + bajo()
            elif(rfm >= 13 and rfm < 25):
                texto = texto + saludable()
            elif(rfm >= 25 and rfm < 30):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        else:
            texto = texto + noEdadRango()

        return texto    

def IAC(clase):
    # Índice de adiposidad corporal
    ## IAC = ((100 * perímetro cadera (m.)) / (altura (m.) * sqrt(altura(m.)))) - 18
    ## Resultado similar al Porcentaje de Grasa Corporal (no es el de arriba)
    ## PGC mide la: grasa esencial + de almacenamiento
    # Ánalisis Resultados: http://altorendimiento.com/indice-de-adiposidad-corporal/

    texto = ""

    def bajo(): return ("\n\nNivel de grasa: **Bajo en grasa**")
    def saludable(): return ("\n\nNivel de grasa: **Saludable**")
    def sobrepeso(): return ("\n\nNivel de grasa: **Sobrepeso**")
    def obesidad(): return ("\n\nNivel de grasa: **Obesidad**")
    def noRangoEdad(): return ("\n\nLas edades aceptadas para el cálculo son desde los 20 hasta los 79 años.")

    iac = (clase.cadera / ((clase.altura / 100) * sqrt((clase.altura / 100)))) - 18
    iac = round(iac,2)
    texto = texto + h2 + "Índice de Adiposidad General: " + bold(str(iac))
    texto = texto + h3 + "Descripción:"
    texto = texto + "\n\nEl IAC da un resultado similar al Porcentaje de Grasa Corporal."
    texto = texto + "\n\nMide la grasa esencial necesaria para realizar las funciones vitales, junto con la grasa de almacenamiento."
    texto = texto + h3 + "Resultado:"
    if(clase.sexo == "M"):
        if (clase.edad in range(20,40)):
            if (iac < 21):
                texto = texto + bajo()
            elif(iac >= 21 and iac < 33):
                texto = texto + saludable()
            elif(iac >= 33 and iac < 39):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(40,60)):
            if (iac < 23):
                texto = texto + bajo()
            elif(iac >= 23 and iac < 35):
                texto = texto + saludable()
            elif(iac >= 35 and iac < 41):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(60,80)):
            if (iac < 25):
                texto = texto + bajo()
            elif(iac >= 25 and iac < 38):
                texto = texto + saludable()
            elif(iac >= 38 and iac < 43):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        else:
            texto = texto + noRangoEdad()
    else:
        if (clase.edad in range(20,40)):
            if (iac < 8):
                texto = texto + bajo()
            elif(iac >= 8 and iac < 21):
                texto = texto + saludable()
            elif(iac >= 21 and iac < 26):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(40,60)):
            if (iac < 11):
                texto = texto + bajo()
            elif(iac >= 11 and iac < 23):
                texto = texto + saludable()
            elif(iac >= 23 and iac < 29):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        elif (clase.edad in range(60,80)):
            if (iac < 13):
                texto = texto + bajo()
            elif(iac >= 13 and iac < 25):
                texto = texto + saludable()
            elif(iac >= 25 and iac < 31):
                texto = texto + sobrepeso()
            else:
                texto = texto + obesidad()
        else:
            texto = texto + noRangoEdad()
    
    return texto

def IC(clase):
    # Índice de Corpulencia: medida de la delgadez de una persona, común en pediatría.
    ## CI = masa (kg.) / altura(m.)^3
    ## Valor normal: 12

    texto = ""
    tolerancia = 2

    ci = clase.peso / ((clase.altura/100)**3)
    ci = round(ci,2)
    texto = texto + h2 + "Índice de Corpulencia: " +  bold(str(ci))
    texto = texto + h3 + "Descripción:"
    texto = texto + "\n\nEl IC mide la corpulencia o delgadez de una persona."
    texto = texto + "\n\nEs muy usado en pediatría para la evaluación de si la restricción del crecimiento intrauterino de un niño es simétrica o asimétrica."
    texto = texto + "\n\nSe ha demostrado que el IC tiene mayor sensibilidad, especificidad, así como valores predictivos tanto positivos como negativos que el IMC tradicional."
    texto = texto + h3 + "Resultado:"
    if(clase.edad <= 1):
        if(diferencia(ci,24,tolerancia)):
            texto = texto + "\n\nEl resultado se considera un valor **atípico** pues el IC normal para un bebé de 12 meses es 24."
        else:
            texto = texto + "\n\nEl resultado se considera un valor **típico** pues el IC normal para un bebé de 12 meses es 24."
    else:
        if(diferencia(ci,12,tolerancia)):
            texto = texto + "\n\nEl resultado se considera un valor **atípico** pues el IC normal es de 12"
        else:
            texto = texto + "\n\nEl resultado se considera un valor **típico** pues el IC normal es de 12"
    
    return texto

def Agua(clase):
    # Agua Corporal Total: Importante para la homeostásis
    ## Por la fórmula se deducen kg. === l. de agua.
    ## TWB = peso (kg.) * C
    ## C en hombres adultos (no ancianos): 0.6
    ## C en hombres adultos ancianos o desnutridos, mujeres (no ancianas): 0.5
    ## C en mujeres ancianas o mujeres desnutridas: 0.45
    # No puedo tener en cuenta la nutrición
    
    texto = ""

    if(clase.edad < 75):
        if(clase.sexo == "M"):
            C = 0.5
        else:
            C = 0.6
    else:
        if(clase.sexo == "H"):
            C = 0.5
        else:
            C = 0.45
    twb = clase.peso * C
    twb = round(twb,2)
    texto = texto + h2 + "Agua Corporal Total: " + bold(str(twb) + " litros")
    texto = texto + h3 + "Descripción:"
    texto = texto + "\n\nEl TWB (en inglés) es una medida de la cantidad de litros de agua que poseemos en nuestro cuerpo, en relación con el peso total."
    texto = texto + "\n\nEs importante tener buenos niveles de agua para realizar una correcta homeostasis."
    texto = texto + h3 +"Resultado:"
    texto = texto + "\n\nTienes " + bold(str(twb) + " litros") + " de agua de un total de " + bold(str(clase.peso) + " kilos") + " que pesas."

    return texto

def diffDatos(actual,anterior):

    texto = ""

    lActual = [ actual.fecha, actual.peso, actual.altura, actual.pecho, actual.brazo, actual.cintura, actual.cadera, actual.muslo, actual.gemelo, actual.tobillo]
    lAnterior = [ anterior.fecha, anterior.peso, anterior.altura, anterior.pecho, anterior.brazo, anterior.cintura, anterior.cadera, anterior.muslo, anterior.gemelo, anterior.tobillo]

    lDiferencia = [ '' ]
    for i in range(1, len(lActual)):
        diferencia = lAnterior[i] - lActual[i]
        diferencia = round(diferencia,2)
        if(diferencia < 0):
            diferencia = str(diferencia)
            diferencia = diferencia
        elif(diferencia == 0):
            diferencia = str(diferencia)
            diferencia = diferencia
        else:
            diferencia = str(diferencia)
            diferencia = diferencia
        lDiferencia.append(diferencia)

    tabla = tabulate([lAnterior, lActual, lDiferencia], headers=['Fecha', 'Peso (Kg.)', 'Altura (cm.)', 'Pecho (cm.)', 'Brazo (cm.)', 'Cintura (cm.)', 'Cadera (cm.)', 'Muslo (cm.)', 'Gemelo (cm.)', 'Tobillo (cm.)'], stralign="center", tablefmt="pipe")
    texto = texto +  "\n" + tabla

    return texto

def plots(listaDias):
    dias = []
    peso = []
    altura = []
    pecho = []
    brazo = []
    cintura = []
    cadera = []
    muslo = []
    gemelo = []
    tobillo = []
    for i in range(len(listaDias)):
        dias.append(listaDias[i].fecha)
        peso.append(listaDias[i].peso)
        altura.append(listaDias[i].altura)
        pecho.append(listaDias[i].pecho)
        brazo.append(listaDias[i].brazo)
        cintura.append(listaDias[i].cintura)
        cadera.append(listaDias[i].cadera)
        muslo.append(listaDias[i].muslo)
        gemelo.append(listaDias[i].gemelo)
        tobillo.append(listaDias[i].tobillo)

    # Cambio días para que Matplotlib lo acepte
    dias = [dt.datetime.strptime(d,'%d-%m-%Y').date() for d in dias]

    def grafica(variable, ylabel, output):
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=intervaloDiasMuestra))
        plt.plot(dias,variable)
        plt.gcf().autofmt_xdate()
        plt.xlabel('Fecha')
        plt.ylabel(ylabel)
        plt.grid(True)
        plt.savefig(output)
        plt.close()

    texto = ""

    def auto(texto):
        t = "\n\n## " + texto + ":\n" + imagen(str(texto),"./" + str(texto) + ".png")
        return(t)

    # Peso (Kg.)
    grafica(peso,"Peso (Kg.)","output/Peso.png")
    texto = texto + auto("Peso")

    # Altura (cm.)
    grafica(altura,"Altura (cm.)","output/Altura.png")
    texto = texto + auto("Altura")
    
    # Perímetro del pecho (cm.)
    grafica(pecho,"Pecho (cm.)","output/Pecho.png")
    texto = texto + auto("Pecho")

    # Perímetro del brazo (cm.) 
    grafica(brazo,"Brazo (cm.)","output/Brazo.png")
    texto = texto + auto("Brazo")

    # Perímetro del cintura (cm.)
    grafica(cintura,"Cintura (cm.)","output/Cintura.png")
    texto = texto + auto("Cintura")

    # Perímetro de la cadera (cm.)
    grafica(cadera,"Cadera (cm.)","output/Cadera.png")
    texto = texto + auto("Cadera")

    # Perímetro del muslo (cm.)
    grafica(muslo,"Muslo (cm.)","output/Muslo.png")
    texto = texto + auto("Muslo")

    # Perímetro del gemelo (cm.)
    grafica(gemelo,"Gemelo (cm.)","output/Gemelo.png")
    texto = texto + auto("Gemelo")

    # Perímetro del tobillo (cm.)
    grafica(tobillo,"Tobillo (cm.)","output/Tobillo.png")
    texto = texto + auto("Tobillo")

    return texto

