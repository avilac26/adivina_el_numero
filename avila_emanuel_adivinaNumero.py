#Tarea 6 Introducción a la Programación
#Estudiante: Emanuel Ávila Córdoba
#Fecha de entrega: 26 de abrril de 2025

#=========================================
#IMPORTACIONES
#=========================================
import tkinter as tk     #Se importa la biblioteca tkinter para generar interfaz gráfica
import random            #Se importa el módulo random para generar números aleatorios

#=========================================
#FUNCIONES
#=========================================

def generar_numero():                  #Se crea la función para generar un número para el juego
    return random.randint(1,100)       #Retorna un número aleatorio del 1 al 100 con el módulo random

def comprobar_numero():                                                        #Se crea la función para comprobar si el intento del usuario es igual al número secreto
    try:                                                                         
        numero_intentado=int(Entrada_intento.get().strip())                           #Se obtiene la entrada del usuario y se eliminan espacios en blanco
    except ValueError:                                                                 #Manejo de error en caso de que el usuario no ingrese un número válido               
        etiqueta_resultado2.config(text="Digita un número válido.")                     #Se genera el resultado y se cambia la etiqueta       
        return                                                                          #Retorno para volver a ingresar un número
    if numero_intentado < 1 or numero_intentado > 100:                                  #Condicional si el intento es fuera del rango solicitado
        etiqueta_resultado2.config(text="Digita un número dentro del rango.")             #Se genera el resultado y se cambia la etiqueta   
    elif numero_intentado > numero_secreto:                                                  #Condicional si el intento del usuario es mayor que el número secreto
        etiqueta_resultado2.config(text="Intenta un número más bajo.")                        #Se genera el resultado y se cambia la etiqueta   
        sumar_intento()                                                                       #Se lleva a cabo la función para sumar un intento
    elif numero_intentado < numero_secreto:                                                     #Condicional si el intento del usuario es menor que el número secreto
        etiqueta_resultado2.config(text="Intenta un número más alto.")                               #Se genera el resultado y se cambia la etiqueta   
        sumar_intento()                                                                           #Se lleva a cabo la función para sumar un intento
    else:                                                                                                               #Condicional si el intento del usuario es igual al número secreto
        etiqueta_resultado2.config(text="¡Correcto! Adivinaste el número secreto: "+ str(numero_secreto))               #Se genera el resultado y se cambia la etiqueta   
        sumar_intento()                                                                                      #Se lleva a cabo la función para sumar un intento
        boton_comprobar.config(state="disabled")                                                          #Se bloquea el botón comprobar para dar a entender que el juego terminó
        ventana.unbind("<Return>")                                                                    #Se desenlaza el botón comprobar con la tecla "Enter"
    Entrada_intento.delete(0, tk.END)                                                             #Se borra la entrada del usuario para ingresar el próximo intento

def sumar_intento():                                                  #Se crea la función para sumar los intentos a medida que el usuario trata de adivinar
    intentos = int(etiqueta_intentos2.cget("text"))                   #Se toma el valor que hay en la etiqueta de intentos
    intentos += 1                                                     #Se suma un intento
    etiqueta_intentos2.config(text=intentos)                          #Se edita la etiqueta de intentos

def nueva_partida():                                                      #Se crea la función para generar una nueva partida
    ventana.bind("<Return>", lambda event: comprobar_numero())            #Se asocia el botón comprobar a la tecla física "Enter" 
    boton_comprobar.config(state="normal")                                #Se habilita de nuevo el botón comprobar
    global numero_secreto                                                 #Se nombra de forma global la variable numero_secreto para poder generar un nuevo número
    numero_secreto = generar_numero()                                     #Se genera un nuevo número secreto
    etiqueta_intentos2.config(text="0")                                   #Se reinicia la etiqueta de cantidad de intentos
    etiqueta_resultado2.config(text="")                                   #Se reinicia la etiqueta de resultados
    Entrada_intento.delete(0, tk.END)                                     #Se borra la entrada del usuario para ingresar el próximo intento


#=========================================
#CONFIGURACION DE LA VENTANA
#=========================================
ventana = tk.Tk()                                 #Se crea la ventana del programa
ventana.title("Adivina el Número")                #Se le asigna el título a la ventana
ventana.geometry("500x200")                       #Se le asigna el tamaño a la ventana

ventana.columnconfigure(0, weight=1)              #Configuración de distribución de columna
ventana.columnconfigure(1, weight=1)              #Configuración de distribución de columna
ventana.columnconfigure(2, weight=1)              #Configuración de distribución de columna

#=========================================
#SECCION DE WIDGETS
#=========================================
etiqueta_titulo=tk.Label(ventana,text="¡Bienvenido a adivina el número!", font=("Courier New", 12))           #Se crea etiqueta de bienvenida
etiqueta_titulo.grid(row=0, column=0, columnspan=3, sticky="we")                                              #Se posiciona la etiqueta


etiqueta_instrucciones1=tk.Label(ventana,text="Instrucciones: Intenta adivinar el número secreto entre 1 y 100.", font=("Courier New", 9))          #Se crea etiqueta de instrucciones
etiqueta_instrucciones1.grid(row=2, column=0, columnspan=3, sticky="we")                                                                            #Se posiciona la etiqueta

etiqueta_en_blanco=tk.Label(ventana,text="")             #Se crea etiqueta de espacio en blanco
etiqueta_en_blanco.grid(row=3, column=0)                 #Se posiciona la etiqueta

etiqueta_tu_intento=tk.Label(ventana,text="  Tu intento:", font=("Courier New", 8))              #Se crea etiqueta de Tu intento:
etiqueta_tu_intento.grid(row=4, column=0)                                                        #Se posiciona la etiqueta

Entrada_intento=tk.Entry(ventana, justify="center")                 #Se crea la entrada para que el usuario digite los intentos
Entrada_intento.grid(row=4, column=1)                               #Se posiciona la entrada


boton_comprobar = tk.Button(ventana, text="Comprobar", command=comprobar_numero, font=("Courier New", 9))               #Se crea el botón Comprobar con la función asociada: comprobar_numero
boton_comprobar.grid(row=4, column=2)                                                                                   #Se posiciona el botón
ventana.bind("<Return>", lambda event: comprobar_numero())                                                              #Se asocia el botón comprobar a la tecla física "Enter" 

etiqueta_resultado1=tk.Label(ventana,text="  Resultado:", font=("Courier New", 9))                   #Se crea etiqueta de Resultado:
etiqueta_resultado1.grid(row=5, column=0)                                                            #Se posiciona la etiqueta

etiqueta_resultado2=tk.Label(ventana,text="", font=("Courier New", 9))            #Se crea etiqueta de resultado según el intento
etiqueta_resultado2.grid(row=5, column=1)                                         #Se posiciona la etiqueta

etiqueta_intentos=tk.Label(ventana,text="  Intentos:", font=("Courier New", 9))             #Se crea etiqueta de Intentos:
etiqueta_intentos.grid(row=6, column=0)                                                     #Se posiciona la etiqueta

etiqueta_intentos2=tk.Label(ventana,text="0", font=("Courier New", 9))           #Se crea etiqueta de cantidad de intentos con 0 como valor inicial y a modificar 
etiqueta_intentos2.grid(row=6, column=1)                                         #Se posiciona la etiqueta

boton_nueva_partida = tk.Button(ventana, text="Nueva Partida", command=nueva_partida, font=("Courier New", 8))                  #Se crea el botón Nueva Partida con la función asociada: nueva_partida para volver a iniciar el juego
boton_nueva_partida.grid(row=7, column=1)                                                                                       #Se posiciona el botón

#=========================================
#GENERACION DE PROGRAMA
#=========================================

numero_secreto = generar_numero()                  #Se genera un número secreto
ventana.mainloop()                                 #Se genera el ciclo para mantener la ventana abierta