#Código hecho por Kevin Ramos
import random
import math
import numpy as np
import matplotlib.pyplot as plt

#Calcular la margen por año
def margen(x):
  margenT = []
  margenT.append(x)
  #ciclo que iterará los próximos 4 años
  for i in range(4):
    #Se calcula el nuevo margen = margen anterior y disminuye el 4% cada año
    x -= ((x*4)//100)
    margenT.append(round(x,0))
  return margenT

#Acumulada
# Función que genera una observación de la distribución triangular
# triang(a,b,c) parámetros a: mín, c: moda, b: máx
# método usado: inversión

def triangular(ei,moda,ed):
  a=ei
  b=ed
  c=moda
  r=random.random()
  #para x entre a y c, r=(x-a)^2/(b-a)(c-a)
  #si x=a, r=0
  #si x=c, r=(c-a)/(b-a)
  r1=(c-a)/(b-a)
  #print(r)
  if r <=r1:
    obs=a+math.sqrt(r*(b-a)*(c-a))
  else :
    obs=b-math.sqrt((1-r)*(b-a)*(b-c))
  return(int(obs))

#Función para calcular las unidades vendidas por año
def ventas(disminucion):
  ventas = []
  #Ciclo que itera los 5 años
  for i in range(5):
    #En caso de ser el primer año se calcula las unidades vendidas sin disminución y se añade a la lista
    if len(ventas) == 0:
      ventas.append(triangular(50000,75000,85000))
    else:
      #En caso de ser otro año diferente al primero se hace la disminución respectiva usando los porcentajes que entran como parámetros en la función
      anterior = ventas[i-1]
      ventas.append((anterior)-((anterior*disminucion[i])//100))
  return ventas

#Función para saber los porcentajes de la disminución de la demanda
def disminucionDemanda():
  porcentaje = [0]
  #Ciclo que itera los próximos 4 años 
  for i in range(4):
    #Calculamos el porcentaje de disminución con la triangular
    disminucion = triangular(5,8,10)
    porcentaje.append(disminucion)
  return porcentaje

#Función para conocer la contribución y recibirá 2 listas como párametros (las unidades vendidas y la margen de ganancia)
def contribucion(margen,ventas):
  contribuciones = []
  #Ciclo que se iterará en los 5 años
  for i in range(5):
    #Calculamos la contribución como margen*unidades vendidas
    contribu = margen[i] * ventas[i]
    contribuciones.append(contribu)
  return contribuciones

#Función para calcular la depreciación con costo variable
def depreciacion(tipoCosto):
  depreciacionTotal = []
  if tipoCosto == "variable":
    costoDesarrollo = triangular(600,650,850)*1000000
  else:
    costoDesarrollo = 700000000
  #Lo calculamos como costoDesarrollo/VidaUtil
  dep = costoDesarrollo//5
  #En un ciclo que itere los 5 años
  for i in range(5):
    depreciacionTotal.append(dep)
  return depreciacionTotal

#Función para calcular la utilidad antes de impuestos, recibe dos listas como parámetros(contribuciones y depreciación)
def utilidadAImp(contribucion,depreciacion):
  utilidadSinImpuestos = []
  #Ciclo que se itera los 5 años
  for i in range(5):
    #Calculamos la utilidad sin impuestos (contribución-depreciación)
    utilidadNI = contribucion[i] - depreciacion[i]
    utilidadSinImpuestos.append(utilidadNI)
  return utilidadSinImpuestos

#Función para calcular la utilidad después de impuestos (recibe como parámetro la lista de la utilidad sin impuestos)
def utilidadDImp(utilidadAntesImpuestos):
  utilidadConImpuestos = []
  #Ciclo que se itera los 5 años
  for i in range(5):
    #Calculamos la utilidad (utilidad antes de impuestos * 1-tarifa impositiva (0.4))
    utilidadNueva = int(utilidadAntesImpuestos[i] * (1-0.4))
    utilidadConImpuestos.append(utilidadNueva)
  return utilidadConImpuestos

#Función para calcular el flujo de la caja (recibe como parámeros las listas de depreciación y la utilidad después de impuestos)
def flujoCaja(depreciacion, utilidadDespuesImpuestos):
  flujo = []
  #Ciclo para calcular el flujo cada año por 5 años
  for i in range(5):
    #Se calcula el flujo por año (depreciación + utilidadDImpuesto)
    flujoNuevo = depreciacion[i] + utilidadDespuesImpuestos[i]
    flujo.append(flujoNuevo)
  return flujo

#Función para calcular el Valor Presente Neto VPN
def valorPresenteNeto(flujoCaja,interes,periodos):
  vpnTotal = 0
  #Ciclo donde calcularemos el VPN como la sumatoria
  for i in range(5):
    vpnTotal += (flujoCaja[i]/(1+interes)**periodos[i])
  return vpnTotal

#Función para calcular 10000 simulaciones con costos variable (se distribuye triangular)
def simularVPN(n,tipoCosto):
  resultados = []
  for i in range(n):
    disminucion = disminucionDemanda()
    margenSim = margen(4000)
    ventasSim = ventas(disminucion)
    contribucionSim = contribucion(margenSim,ventasSim)
    depreciacionSim = depreciacion(tipoCosto)
    utilidadAntesImpuestosSim = utilidadAImp(contribucionSim,depreciacionSim)
    utilidadDespuesImpuestosSim = utilidadDImp(utilidadAntesImpuestosSim)
    flujoCajaSim = flujoCaja(depreciacionSim,utilidadDespuesImpuestosSim)
    periodos = [1,2,3,4,5]
    interes = 0.1
    #Llamamos y guardamos la lista del VPN (Valor Presente Neto)
    vpnSim = valorPresenteNeto(flujoCajaSim,interes,periodos)
    resultados.append(vpnSim)
  return resultados

#Función para calcular el número N de simulaciones requeridas
def calcularN(tipoCosto):
  #Simular 10000 veces VPN
  muestra10k = simularVPN(10000, tipoCosto)
  #Calcular la desviación estándar de la muestra
  desviacion = np.std(muestra10k)
  #Número de precisión dado por el ejercicio
  precision = 1000000
  #Valor de X para el nivel de confianza 95%
  z = 1.96
  #Usar la fórmula para hallar el número n requerido
  n = ((z**2) * (desviacion**2)) / (precision**2)
  #retornamos los valores
  return int(n),desviacion

#PARTE MAIN DEL CÓDIGO
nRequerido, desviacion = calcularN("fijo")
print()
print("De una muestra de 10000 simulaciones con costo fijo, la desviación estándar de dicha muestra es de: ", desviacion)
print("El número de simulaciones requeridas es: ", nRequerido)
resultadosFijo = simularVPN(nRequerido,"fijo")

# Cálculo del intervalo de confianza del 95%
desVPNFIJO = np.std(resultadosFijo)
mediaVPNFIJO = np.mean(resultadosFijo)
margenError = 1.96 * (desVPNFIJO / math.sqrt(nRequerido))
ic_inferior = mediaVPNFIJO - margenError
ic_superior = mediaVPNFIJO + margenError
print("IC 95% Inferior: ", ic_inferior)
print("IC 95% Superior: ", ic_superior)
print("La media para VPNs con costo fijo es: ",mediaVPNFIJO)
print()

nRequerido2, desviacion2 = calcularN("variable")
print("De una muestra de 10000 simulaciones con costo variable, la desviación estándar de dicha muestra es de: ", desviacion2)
print("El número de simulaciones requeridas es: ", nRequerido2)
resultadosVar = simularVPN(nRequerido2,"variable")

# Cálculo del intervalo de confianza del 95%
desVPNVAR = np.std(resultadosVar)
mediaVPNVAR = np.mean(resultadosVar)
margenError2 = 1.96 * (desVPNVAR/ math.sqrt(nRequerido2))
ic_inferior2 = mediaVPNVAR - margenError2
ic_superior2 = mediaVPNVAR + margenError2
print("IC 95% Inferior: ", ic_inferior2)
print("IC 95% Superior: ", ic_superior2)
print("La media para VPNs con costo variable es: ",mediaVPNVAR)
print()

# Crear el histograma
plt.figure(figsize=(10, 6))
plt.hist(resultadosFijo, bins=30, color='blue', alpha=0.7, label='VPNs con costo fijo')
plt.hist(resultadosVar, bins=30, color='orange', alpha=0.7, label='VPNs con costo variable')
# Etiquetas y leyenda
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.title('Distribución de los VPNs para costos fijos y variables')
plt.legend(loc='upper left')
# Mostrar el gráfico
plt.show()