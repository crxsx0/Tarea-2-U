import random
import pandas as pd
import matplotlib.pyplot as plt
import os


alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
archivo_equipos = open("equipos.csv", "w")

def revision(palabra):
    x=False
    while x==False:
        for i in palabra:
            x= False
            for y in alfabeto:
                if i.lower() == y:
                    x= True
                    break
            if x!=True:
                break
        
        if x==False:
            palabra= str(input("Ingrese el dato nuevamente: "))
    return str(palabra)

def revision_edad_input(edad):
    try:
        int(edad)
        return True
    except ValueError:
        return False

def revision_edad(edad):
    while revision_edad_input(edad) == False:
        edad=input("Ingrese el dato nuevamente: ")
    return str(edad)

def revision_opcion(opcion):
    while revision_edad_input(opcion) == False:
        opcion=input("Ingrese el dato nuevamente: ")
    return int(opcion)

for i in range(3):
    lista_equipos = ["nombre","equipo","edad"]
    archivo_equipos.write(lista_equipos[i])
    if i != 2:
        archivo_equipos.write(",")
    elif i == 2:
        archivo_equipos.write("\n")

archivo_equipos.close

a = 1
#while para agregar mas piloto
print("Puedes agregar hasta 20 pilotos")

while a <= 20:
    with open("equipos.csv", "a") as archivo_equipos:
        a = a + 1
        pilot = str(input("Ingrese el nombre del piloto: "))
        pilot = revision(pilot)
        archivo_equipos.write(pilot)
        archivo_equipos.write(",")
        team = str(input("Ingrese el equipo: "))
        team = revision(team)
        archivo_equipos.write(team)
        archivo_equipos.write(",")
        edad = input("Ingrese su edad: ")
        edad = revision_edad(edad)
        archivo_equipos.write(edad)
        archivo_equipos.write("\n")
    archivo_equipos.close()
    d = True
    
    while d == True:
        opcion_lista = [1,2,3]
        opcion = input("Que opcion desea?\nDigite 1 para agregar pilotos\nDigite 2 para no agregar mas pilotos\nDigite 3 para eliminar pilotos: ")
        opcion = revision_opcion(opcion)
        e = True
        while e==True:
            if opcion < 0 or opcion > 3:
                opcion = input("Digite 1 para agregar pilotos\nDigite 2 para no agregar mas pilotos\nDigite 3 para eliminar pilotos\nIngrese la opcion nuevamente: ")
                opcion = revision_opcion(opcion)
            else:
                e = False
            
        if opcion == 3:
            df_team =  pd.read_csv("equipos.csv")
            print(df_team)
            os.remove("equipos.csv")
            cantidad_eliminar = df_team.shape[0]
            u = True
            while u == True:
                eliminar = input("Ingrese el numero del piloto que desea eliminar: ")
                eliminar = revision_opcion(eliminar)
                if eliminar < 0 or eliminar > cantidad_eliminar:
                    eliminar = input("Ingrese el numero del piloto que desea eliminar: ")
                    eliminar = revision_opcion(eliminar)
                else:
                    u = False
            df_team = df_team.drop([eliminar])
            df_team.to_csv("equipos.csv", index=False)
            df_team = pd.read_csv("equipos.csv")
            print("piloto eliminado satisfactoriamente\n")
            d = False

        elif opcion == 2:
            a = 21
            d = False
        elif opcion == 1:
            d = False


#class piloto donde haremos los tiempos de los pilotos 
class pilotos:
    def __init__(self, nombre, equipo, edad):
        self.nombre = nombre
        self.equipo = equipo
        self.edad = edad
    
    def __str__(self):
        return "Equipo: " + self.equipo + " Edad: " + str(self.edad)
        
    random.seed()
    def monaco(self):
        #tiempo de los pilotos
        resultados=[self.nombre, self.equipo, self.edad]
        for i in range(13):
            i = random.uniform(1.12, 1.19)
            i = round(i,2)
            resultados.append(i)
        tiempo_final = resultados[15] #tiempo_final = resultado[-1]
        #archivos 
        with open("resultado_monaco.csv", "a") as c:
            for i in range(16):
                c.write(str(resultados[i]))
                if i != 15:
                    c.write(",")
                elif i == 15:
                    c.write("\n")
            c.close()
        return tiempo_final
        
    def silverstone(self):
        #tiempo de los pilotos
        resultados=[self.nombre, self.equipo, self.edad]
        for i in range(13):
            i = random.uniform(1.24, 1.31) 
            i = round(i,2)
            resultados.append(i)
        tiempo_final = resultados[15] 
        #archivos 
        with open("resultado_silverstone.csv", "a") as c:
            for i in range(16):
                c.write(str(resultados[i]))
                if i != 15:
                    c.write(",")
                elif i == 15:
                    c.write("\n")
            c.close()
        return tiempo_final

    def spa(self):
        #tiempo de los pilotos
        resultados=[self.nombre, self.equipo, self.edad]
        for i in range(13):
            i = random.uniform(1.4, 1.51) 
            i = round(i,2)
            resultados.append(i)
        tiempo_final = resultados[15] 
        #archivos    
        with open("resultado_spa.csv", "a") as c:
            for i in range(16):
                c.write(str(resultados[i]))
                if i != 15:
                    c.write(",")
                elif i == 15:
                    c.write("\n")
            c.close()
        return tiempo_final

    def zandvoort(self):
        #tiempo de los pilotos
        resultados=[self.nombre, self.equipo, self.edad]
        for i in range(13):
            i = random.uniform(1.09, 1.15) 
            i = round(i,2)
            resultados.append(i)
        tiempo_final = resultados[15] 
        #archivos 
        with open("resultado_zandvoort.csv", "a") as c:
            for i in range(16):
                c.write(str(resultados[i]))
                if i != 15:
                    c.write(",")
                elif i == 15:
                    c.write("\n")
            c.close()
        return tiempo_final
    
    def abudhabi(self):
        #tiempo de los pilotos
        resultados=[self.nombre, self.equipo, self.edad]
        for i in range(13):
            i = random.uniform(1.24, 1.42) 
            i = round(i,2)
            resultados.append(i)
        tiempo_final = resultados[15] 
        #archivos 
        with open("resultado_abudhabi.csv", "a") as c:
            for i in range(16):
                c.write(str(resultados[i]))
                if i != 15:
                    c.write(",")
                elif i == 15:
                    c.write("\n")
            c.close()
        return tiempo_final

def resultado_pista(c):
    fila_1_resultados = ["nombre","equipo","edad","L1","L2","L3","L4","L5","L6","L7","L8","L9","L10","L11","L12","L13"]
    for i in range(5):
        with open("resultado_"+c+".csv", "w") as ab:
            for i in range(16):
                ab.write(str(fila_1_resultados[i]))
                if i != 15:
                    ab.write(",")
                elif i == 15:
                    ab.write("\n")
            ab.close()

def pista_piloto(i):
    df = pd.read_csv("equipos.csv")
    nombre = df.iloc[i]["nombre"]
    equipo = df.iloc[i]["equipo"]
    edad = df.iloc[i]["edad"]
    piloto = pilotos(nombre,equipo,edad)
    monaco = pilotos.monaco(piloto)
    silver = pilotos.silverstone(piloto)
    spa = pilotos.spa(piloto)
    zand = pilotos.zandvoort(piloto)
    abu = pilotos.abudhabi(piloto)
    tracks = [nombre,monaco,silver,spa,zand,abu]     
    return tracks
        
#----------------------------------------------------------------------
pistas = ["monaco","silverstone","spa","zandvoort","abudhabi"]

for i in pistas:
    resultado_pista(i)
track = ["Nombres","monaco","silverstone","spa","zandvoort","abudhabi"]
with open("tracks.csv", "w") as tracks:
    for i in range (6):
        tracks.write(track[i])
        if i != 5:
            tracks.write(",")
        elif i == 5:
            tracks.write("\n")
    tracks.close()

teams = pd.read_csv("equipos.csv")
cantidad_pilotos = teams.shape[0]

for i in range(cantidad_pilotos):
    a = pista_piloto(i)
    with open("tracks.csv", "a") as tracks:
        for x in range(6):
            tracks.write(str(a[x]))
            if x != 5:
                tracks.write(",")
            elif x == 5:
                tracks.write("\n")
        tracks.close()

print("\n")
print(pd.read_csv("tracks.csv", index_col="Nombres"))

def pilotosss():
    df = pd.read_csv("tracks.csv")
    lista = []
    for x in range(cantidad_pilotos):
        lista.append(str(df.iloc[x]["Nombres"]))
    return lista

def grafico():
    df = pd.read_csv("tracks.csv", index_col=0)
    df = df.transpose()
    df.plot()
    plt.xlabel("Pistas")
    plt.title("Competencia")     
    plt.savefig("tracks.png")
    plt.show()

pilotoss = pilotosss()

grafico()


''' ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿tabom⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣩⣭⣶⣶⣮⣭⡙⠿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⠿⣋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡃⠄⠹⡿⣿⣿⣿⣿⠟⠛⣿⣿⣿⣿⣷⡌⢿⣿⣿
    ⣿⣿⣿⣿⣿⠐⣠⡶⣶⣲⡎⢻⣿⣤⣴⣾⣿⣿⣿⣿⣿⠸⣿⣿
    ⣿⠟⣋⡥⡶⣞⡯⣟⣾⣺⢽⡧⣥⣭⣉⢻⣿⣿⣿⣿⣿⣆⢻⣿
    ⡃⣾⢯⢿⢽⣫⡯⣷⣳⢯⡯⠯⠷⠻⠞⣼⣿⣿⣿⣿⣿⣿⡌⣿
    ⣦⣍⡙⠫⠛⠕⣋⡓⠭⣡⢶⠗⣡⣶⡝⣿⣿⣿⣿⣿⣿⣿⣧⢹
    ⣿⣿⣿⣿⣿⣿⣘⣛⣋⣡⣵⣾⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⢸
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⢸'''
