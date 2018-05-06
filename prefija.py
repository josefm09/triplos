# -*- coding: utf-8 -*-
import sys
import re
#example (6+4)*8(7+4)
print('Declare una expresion')
#ex = str(input()) #se almacena la expresion
ex = '(6+4)*(7+4)'
valid = False #se inicializa una variable en falso, luego se utilizara
pila = [] #se inicializa la pila 
resultado = [] #se inicializa el arreglo de resultados
orderRes = '' #se inicializa el string del resultado ordenado
def prefija(value): #se declara la funcion prefija que lleva por parametro un valor
    for i in value: #se inicia un ciclo con el tamaño de la expresion
        if re.match('[a-zA-Z0-9-/?+?*?(?)]',i): #se pregunta si es una expresion correcta con expresiones regjulares
            valid = True #se cambia el valor a verdadero para seguir
        else: #si no termina el programa
            print('ingrese una expresion valida') 
            sys.exit()
    if valid:#si es valido continua la funcion
        value = value[::-1] #se invierte el orden de la expresion
        for j in value: #se inicia un ciclo para recorrer la expresion 
            if j in '+-*/)': #se buscan los operadores en la expresion
                pila.append(j) #si se encuentran se agregan a la pila
            if re.match('[a-zA-Z0-9]',j): #se buscan los numeros en la expresionm y las letras
                resultado.append(j) #se agregan al resultado
            if j == '(': #se busca en cierre de parentesis
                while pila: #se inicia un ciclo que mientras haya elementos en la pila 
                    resultado.append(pila.pop()) #se añadiran los elementos ultimos de la pila al resultado
        for n in resultado: #se recorre el resultado para eliminar los parentesis de cierre
            if n == ')':#si se encuentra 
                resultado.remove(n)#se elimina
prefija(ex)# se ejecuta la funcion
for n in reversed(resultado): #se recorre el resultado invertido 
    orderRes += n#para añadir los valores a un string

def triplo(value): #se declara la función que regresa las variables intermedias
    operador = [] #Arreglo para almacenar los operadores
    intermedia = [] #Arreglo para almacenar los nombres de las variables intermedias
    con = 0 #contador  para manejar la interación de el contenido de la pila que contiene los alfanumericos al revez
    c = 1 #contador para controlar el orden en que se leen los operadores
    ci = 0 #contador para controlar el orden de las variables intermedias
    nuevo = '' #se inicializan la variable en la que se concatenan el resultado de voltear la pila alfanumerica
    for i in value: #ciclo que recibe el parametro del metodo que contiene la pila resultado completa
        if re.match('[a-zA-Z0-9]',i): #se valida que contenga caracteres alfanumericos para separar los operadores de los operandos
            pila.append(i) #se agregan en el arreglo pila los caracteres que son operandos
        if i in '+-*/)': #Se valida que sea un operador el siguiente elemento
            operador.append(i) #Se agregan los operadores al arreglo operador
    
    for n in reversed(pila): #se invierte y recorre la pila de los operandos    
        nuevo += n#se almacena en una nueva variable de tipo string el resultado
        
    try: 
        for j in nuevo: #se recorre la nueva variable 
            if con < len(nuevo): #comparamos que el contador sea menor a la longitud de la varible
                aux1 = nuevo[con] #almacenamos el caracter introducido 
                aux2 = nuevo[con + 1] #almacenamos el otro operando

            else: #si superamos la longitud de la variable entonces tenemos variables intermedias
                aux1 = intermedia[ci] #almacenamos la variable intermedia con la posicion de su propio contador
                ci += 1 #aumentamos el contador
                aux2 = intermedia[ci] #para seguir con lasiguiente variable intermedia
            
            cadena = '%s%s%s%s%s%s' % ('T',c,' = ',aux1,operador[c-1],aux2) #creaamos una cadena preparada segun los resultados de la validacion
            print(cadena) #imprimimos la cadena preparada para visualizar el codigo intermedio
            intermedia.append(cadena[:2]) #agregamos a la pila de variables intermedias el nombre de la siguiente variable
            con += 2 #aumentamos los contadores de manera independiente
            c += 1
    except IndexError:
        print("") #capturamos las excepciones
        source = ""    
    

triplo(resultado)# se ejecuta la función para imprimir los triplos

print('Notacion infija ', ex)#se imprime la expresion original
print('Notacion prefija ',orderRes)#se imprime la expresion en prefija




                
