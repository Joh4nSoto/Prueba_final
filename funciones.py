import random
import os
import time
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos = []
for trabajador in trabajadores:
    sueldorandom = round(random.randint(300000,2500000))
    sueldos.append(sueldorandom)
def limpiar():
    os.system("cls")
def opcion():
    opc = int(input("Seleccione una opcion: "))
    return opc
def menu_1():
    print("-----Empleados-----")
    print("1) Asignar sueldos aleatorios")
    print("2) Clasificar sueldos")
    print("3) Ver estadisticas")
    print("4) Reporte de sueldos")
    print("5) Exportar csv")
    print("0) Salir del programa")
def asignar_sueldo():
    for i in range(len(trabajadores)):
        print(f"nombre: {trabajadores[i]}, sueldos: ${sueldos[i]}")
    print("Se han asignado sueldos aleatorios con exito!.")
    print("Presiona una tecla para volver.")
    opcion()
def clasificar_sueldo():
    sueldos_menores = 0
    sueldos_entre = 0
    sueldos_superiores = 0
    total_sueldo = 0
    for posicion, trabajador in enumerate(trabajadores):
        if sueldos[posicion] < 800000 :
            sueldos_menores += 1
            menores = []
            menores.append(trabajador)
        if 2000000 > sueldos[posicion] > 800000 :
            sueldos_entre += 1
            entre = []
            entre.append(trabajador)
        if sueldos[posicion] > 2000000 :
            sueldos_superiores += 1
            superiores = []
            superiores.append(trabajador)
        total_sueldo += sueldos[posicion]
    print(f"Sueldos menores a $800.000 \nTOTAL: {sueldos_menores}")
    print("Nombre empleado | Sueldo")
    for i in range(len(menores)):
        print(menores[i])
    print(f"Sueldos entre $800.000 y $2.000.000 \nTOTAL: {sueldos_entre}")
    print("Nombre empleado | Sueldo")
    for i in range(len(entre)):
        print(entre[i])
    print(f"Sueldos superiores a $2.000.000 \nTOTAL: {sueldos_superiores}")
    print("Nombre empleado | Sueldo")
    for i in range(len(superiores)):
        print(superiores[i])
    print(f"TOTAL SUELDOS: ${total_sueldo}")
    print("Presiona una tecla para volver.")
    opcion()
def ver_estadisticas():
    print(f"el sueldo mayor es de ${sueldo_mayor()}")
    print(f"el sueldo menor es de ${sueldo_menor()}")
    print(f"el promedio de sueldo es de ${sueldo_promedio()}")
    print(f"la media gemotrecia es de ${media_geometrica()}")
    print("Presiona una tecla para volver.")
    opcion()
def sueldo_mayor():
    sueldo_mayor = sueldos[0]
    for sueldo in sueldos:
        if sueldo > sueldo_mayor:
            sueldo_mayor = sueldo
    return sueldo_mayor
def sueldo_menor():
    sueldo_menor = sueldos[0]
    for sueldo in sueldos:
        if sueldo < sueldo_menor:
            sueldo_menor = sueldo
    return sueldo_menor
def sueldo_promedio():
    sueldo_total = 0
    for sueldo in sueldos:
        sueldo_total += sueldo
    sueldo_promedio = sueldo_total/len(sueldos)
    return round(sueldo_promedio)
def media_geometrica():
    sueldo_multi = sueldos[0]
    for sueldo in sueldos:
        sueldo_multi *= sueldo 
        mediageometrica = sueldo_multi ** (1/10)
    return round(mediageometrica)
def reporte_sueldos():
    print(" NOMBRE EMPLEADO        SUELDO BASE       DESCUENTO SALUD      DESCUENTO AFP      SUELDO LIQUIDO")
    for i in range(len(trabajadores)):
        print(f"{trabajadores[i]}              ${round(sueldos[i])}              ${round(sueldos[i]*0.93)}            ${round(sueldos[i]*0.88)}          ${round(sueldos[i]*0.81)}")
    opcion()
def exportar_trabajadores():
    with open("trabajadores.csv","w") as trabajador:
        trabajador.write(trabajadores)
def exportar_sueldos():
    with open("sueldos.csv","w") as sueldo:
        sueldo.write(sueldos)