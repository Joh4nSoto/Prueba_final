from funciones import *
while True:
    limpiar()
    menu_1()
    try:
        opc = opcion()
        match opc:
            case 1:
                limpiar()
                asignar_sueldo()
            case 2:
                limpiar()
                clasificar_sueldo()
            case 3:
                limpiar()
                ver_estadisticas()
            case 4:
                limpiar()
                reporte_sueldos()
            case 5:
                limpiar()
                exportar_trabajadores()
                exportar_sueldos()
            case 0:
                break
    except:
        print("Error, vuelva a ingresar nuevamente.")