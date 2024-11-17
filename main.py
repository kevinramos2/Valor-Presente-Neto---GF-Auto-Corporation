#Código hecho por Kevin Ramos
import random
import math

#Calcular la margen por año
def margen(x):
  #Iniciamos la lista que almacenará el margen por año
  margenT = []
  #Añadimos el parámetro que ingresa a la función como la margen inicial en los 5 años
  margenT.append(x)
  #ciclo que iterará los próximos 4 años
  for i in range(4):
    #Se calcula el nuevo margen = margen anterior y disminuye el 4% cada año
    x -= ((x*4)//100)
    #Añadimos el nuevo margen a la lista
    margenT.append(round(x,0))
  #Retornamos la lista
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
  #Inicializamos la lista de ventas 
  ventas = []
  #Ciclo que itera los 5 años
  for i in range(5):
    #En caso de ser el primer año se calcula las unidades vendidas sin disminución y se añade a la lista
    if len(ventas) == 0:
      ventas.append(triangular(50000,75000,85000))
    else:
      #En caso de ser otro año diferente al primero se hace la disminución respectiva usando los porcentajes que entran como parámetros en la función
      anterior = ventas[i-1]
      #Se agregan las unidades vendidas a la lista ventas
      ventas.append((anterior)-((anterior*disminucion[i])//100))
  #Retornamos la lista
  return ventas

#Función para saber los porcentajes de la disminución de la demanda
def disminucionDemanda():
  #Iniciamos la lista con los porcentajes de disminución con el valor del primer año en 0
  porcentaje = [0]
  #Ciclo que itera los próximos 4 años 
  for i in range(4):
    #Calculamos el porcentaje de disminución con la triangular
    disminucion = triangular(5,8,10)
    #Añadimos el porcentaje calculado a la lista
    porcentaje.append(disminucion)
  #Retornamos la lista
  return porcentaje

#Función para conocer la contribución y recibirá 2 listas como párametros (las unidades vendidas y la margen de ganancia)
def contribucion(margen,ventas):
  #Iniciamos la lista con las contribuciones vacía
  contribuciones = []
  #Ciclo que se iterará en los 5 años
  for i in range(5):
    #Calculamos la contribución como margen*unidades vendidas
    contribu = margen[i] * ventas[i]
    #Añadimos la contribución por año a la lista
    contribuciones.append(contribu)
  #Retornamos la lista de las contribuciones
  return contribuciones

#Función para calcular la depreciación
def depreciacion():
  #Iniciamos la lista que contendrá la depreciación en cada año
  depreciacionTotal = []
  #Al ser un valor constante lo calculamos como costoDesarrollo/VidaUtil
  dep = 700000000//5
  #En un ciclo que itere los 5 años
  for i in range(5):
    #Añadimos el mismo valor a la lista
    depreciacionTotal.append(dep)
  #Retornamos la lista de la depreciación
  return depreciacionTotal

#Función para calcular la utilidad antes de impuestos, recibe dos listas como parámetros(contribuciones y depreciación)
def utilidadAImp(contribucion,depreciacion):
  #Lista donde se guardará la utilidad sin impuestos
  utilidadSinImpuestos = []
  #Ciclo que se itera los 5 años
  for i in range(5):
    #Calculamos la utilidad sin impuestos (contribución-depreciación)
    utilidadNI = contribucion[i] - depreciacion[i]
    #La añadimos a la lista
    utilidadSinImpuestos.append(utilidadNI)
  #Retornamos la lista con la utilidad sin impuestos
  return utilidadSinImpuestos

#Función para calcular la utilidad después de impuestos (recibe como parámetro la lista de la utilidad sin impuestos)
def utilidadDImp(utilidadAntesImpuestos):
  #Iniciamos la lista de la utilidad con impuestos
  utilidadConImpuestos = []
  #Ciclo que se itera los 5 años
  for i in range(5):
    #Calculamos la utilidad (utilidad antes de impuestos * 1-tarifa impositiva (0.4))
    utilidadNueva = int(utilidadAntesImpuestos[i] * (1-0.4))
    #Añadimos a la lista de utilidad
    utilidadConImpuestos.append(utilidadNueva)
  #Retornar la lista
  return utilidadConImpuestos

#Función para calcular el flujo de la caja (recibe como parámeros las listas de depreciación y la utilidad después de impuestos)
def flujoCaja(depreciacion, utilidadDespuesImpuestos):
  #Lista que contendrá el flujo de la caja en los 5 años
  flujo = []
  #Ciclo para calcular el flujo cada año por 5 años
  for i in range(5):
    #Se calcula el flujo por año (depreciación + utilidadDImpuesto)
    flujoNuevo = depreciacion[i] + utilidadDespuesImpuestos[i]
    #Añadimos el flujo a la lista
    flujo.append(flujoNuevo)
  #Retornamos la lista
  return flujo

#Función para calcular el Valor Presente Neto VPN
def valorPresenteNeto(flujoCaja,interes,periodos):
  #Variable donde quedará almacenado el valor del VPN
  vpnTotal = 0
  #Ciclo donde calcularemos el VPN por la sumatoria
  for i in range(5):
    vpnTotal += int(flujoCaja[i]//(1+interes)**periodos[i])
    print(vpnTotal)
  #Retornamos el valor del VPN
  return vpnTotal

#Llamamos y guardamos la lista de porcentajes de disminución
disminucion = disminucionDemanda()
#Llamamos y guardamos la lista del margen por unidad
margen = margen(4000)
#Llamamos y guardamos la lista de las unidades vendidas
ventas = ventas(disminucion)
#Llamamos y guardamos la lista de la contribución
contribucion = contribucion(margen,ventas)
#Llamamos y guardamos la lista de la depreciación
depreciacion = depreciacion()
#Llamamos y guardamos la lista de la utilidad antes de los impuestos
utilidadAntesImpuestos = utilidadAImp(contribucion,depreciacion)
#Llamamos y guardamos la lista de la utilidad después de los impuestos
utilidadDespuesImpuestos = utilidadDImp(utilidadAntesImpuestos)
#Llamamos y guardamos la lista del flujo de la caja
flujoCaja = flujoCaja(depreciacion,utilidadDespuesImpuestos)
#Periodos
periodos = [1,2,3,4,5]
#Interés
interes = 0.1
#Llamamos y guardamos la lista del VPN (Valor Presente Neto)
vpn = valorPresenteNeto(flujoCaja,interes,periodos)
print("La disminución de la demanda es: ", disminucion)
print("Las unidades vendidas en los 5 años es: ",ventas)
#Calculamos el margen en los 5 años
print("El margen en los 5 años es: ",margen)
#Calculamos ahora la contribución
print("La contribución en los 5 años es: ", contribucion)
#Calculamos la depreciación
print("La depreciación en los 5 años es: ", depreciacion)
#Calculamos la utilidad antes de impuestos
print("La utilidad antes de impuestos en los 5 años es: ", utilidadAntesImpuestos)
#Calculamos la utilidad después de impuestos
print("La utilidad después de impuestos en los 5 años es: ", utilidadDespuesImpuestos)
#Calculamos el flujo neto de la caja
print("El flujo neto de la caja es en los 5 años es: ", flujoCaja)
#Calculamos el VPN (Valor Presente Neto)
print("El valor presente neto es: ", vpn )



