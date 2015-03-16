##*******************************************************************************************
## Institulo Tecnológico de Costa Rica
## Análisis de algoritmos
## Código de curso : IC - 3002
## Profesor : Mauricio Rojas Fernández
## 
## PROGRAMA   : Maximos_Arreglo.py
##
## Estudiante : Melissa Molina Corrales.
##
## Carné      : 2013006074
##
## Fecha      : 15/03/2015
##******************************************************************************************

def indices_mayores_arreglo(arreglo): 
    """Imprime el primer y segundo elemento mayor del arreglo
        y sus respectivas posiciones en el arreglo.
        
        Entradas : Un arreglo
        Salidas  : primer y segundo elemento mayor y sus posiciones
        en el arreglo.
        Restricciones :
        El argumento de entrada debe ser un arreglo.
    """

    primer_mayor = maximos_arreglo(arreglo)
    pos_primer_mayor = posicion(primer_mayor, arreglo)
    arreglo.remove(primer_mayor)
        
    segundo_mayor = maximos_arreglo(arreglo)
    pos_segundo_mayor = posicion(segundo_mayor,arreglo)
        
    print("Primer mayor: " + str(primer_mayor))
    print("Posición en el arreglo: " + str(pos_primer_mayor))

    print("Segundo mayor: " + str(segundo_mayor))
    print("Posición en el arreglo: " + str(pos_segundo_mayor))

    
def maximos_arreglo(arreglo):
    if not isinstance(arreglo,list):
        print("Error el argumento de entrada debe ser de tipo list")
    else:
        return maximos_arreglo_aux(arreglo,0,len(arreglo)-1)
    

def maximos_arreglo_aux(arreglo,inicio,fin):
    """ Determina el elemento máximo de un arreglo
        mediante divide y conquista, busca el elemento
        máximo en cada mitad, hasta que la mitad tenga
        un elemento, el cual seria el maximo que seria el
        resultado de la función mayor.
        
        Entradas : Un arreglo
        Salidas  : elemento mayor del arreglo
        Restricciones :
        El argumento de entrada debe ser un arreglo.
    """
    
    if inicio == fin:
        return arreglo[inicio]

    else:
        mitad = (inicio + fin) //2 #Determina a partir de donde se va a dividir el arreglo
        mitad_izquierda = maximos_arreglo_aux(arreglo,inicio,mitad)
        mitad_derecha = maximos_arreglo_aux(arreglo,mitad+1,fin)
        
        return mayor(mitad_izquierda,mitad_derecha)#Determina cual de las 2 partes tiene el elemento mayor

def mayor(num1,num2):
    if not isinstance(num1,int) or not isinstance(num2,int):
        print("Error los argumentos de entrada deben ser un entero")   
    else:
        return mayor_aux(num1,num2)

def mayor_aux(num1,num2):
    """Determina el elemento mayor de acuerdo a los números
        ingresados.
        Entradas : dos números
        Salidas  : número mayor
        Restricciones :
        Los argumentos de entrada deben ser dos números.
    """

    if num1 > num2:
       return num1
    else:
       return num2
    
def posicion(k,L):
    if not isinstance(k,int) or not isinstance(L,list):
        print("Error")
    else:
        return posicion_aux(k,L,0)

def posicion_aux(k,L,ini):
    """Retorna la posición de un elemento en el arreglo

       Entradas: número a buscar y el arreglo
       Salidas : posición del número ingresado en el arreglo
       Restricciones:
       Los argumentos de entrada deben ser un arreglo y un número
    """

    if ini == len(L):
        return False

    elif L[ini] == k:
        return ini
    
    else:
        return posicion_aux(k,L,ini+1)    



















    
