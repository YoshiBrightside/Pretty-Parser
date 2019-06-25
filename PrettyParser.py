# coding=utf-8
import unidecode

archivoInput = open('input.txt')
temp = archivoInput.readline().split('T')
trimestre, anio, provedorActual, cal, conv = int(temp[0]), temp[1][:-1], '', {}, {}
descripciones, total, precioTotal, precioUnitarioBarato, proveedorBarato = [], {}, {}, {}, {}
# Diccionario para obtener meses de forma numerica
cal['ene'], cal['feb'], cal['mar'], cal['abr'] = 1,2,3,4
cal['may'], cal['jun'], cal['jul'], cal['ago'] = 5,6,7,8
cal['sep'], cal['oct'], cal['nov'], cal['dic'] = 9,10,11,12
# Diccionario para definir y obtener conversiones al Sistema Internacional
conv['kg'], conv['m'], conv['m^2'] = 1,1,1
conv['lbs'], conv['ft'], conv['ft^2'] = .4535, .3048, .0929


for line in archivoInput:
    # Ignora las lineas vacias y obtenemos el nombre del siguiente provedor
    if (line == '\n'):
        provedorActual = ''
        continue
    if (provedorActual == ''):
        provedorActual = line[:-1]
        continue
    
    # Prepara la linea.
    # Ignora fechas no correspondientes con trimestre y anio.
    # Quita caracteres especiales, espacios y vuelve todo mayusculas.
    # Quita comas y saltos en numeros.
    temp = line.split('|')
    if ((cal[temp[0].split('-')[1]]+2)//3 != trimestre or temp[0].split('-')[2] != anio):
        continue
    descripcion = ''.join(c for c in unidecode.unidecode(temp[3].decode('utf-8')).upper() if c.isalnum())
    temp[1] = float(temp[1])
    temp[4] = float(temp[4][:-1].replace(",", ""))
    
    # Verifica si la descripción es nueva o no.
    # Actualiza el total, su costo total, y su minimo precio unitario si es el caso.
    precioUnitActual = temp[4]/(temp[1]*conv[temp[2]])
    if (descripcion not in total):
        descripciones.append(descripcion)
        total[descripcion] = temp[1]*conv[temp[2]]
        precioTotal[descripcion] = temp[4]
        proveedorBarato[descripcion] = provedorActual
        precioUnitarioBarato[descripcion] = precioUnitActual
    else:
        total[descripcion] += temp[1]*conv[temp[2]]
        precioTotal[descripcion] += temp[4]
        if (precioUnitarioBarato[descripcion] > precioUnitActual):
            precioUnitarioBarato[descripcion] = precioUnitActual
            proveedorBarato[descripcion] = provedorActual

# Hace un archivo output con los resultados.
outputFile = open('output.txt','w') 
for e in descripciones:
    outputFile.write(e +'|')
    outputFile.write(("%.2f" % total[e]) +'|')
    outputFile.write(("%.2f" % (precioTotal[e]/total[e])) +'|')
    outputFile.write(proveedorBarato[e] +'\n')
outputFile.close()