#=========================================
#IMPORTACIONES
#=========================================
import tkinter as tk        #Se importa la biblioteca tkinter para generar interfaz gráfica
import random             #Se importa el módulo random para generar números aleatorios

#=========================================
# FUNCIONES
#=========================================
def generar_numero():                         #Se crea la función para generar un número para el juego
    return random.randint(1,100)       #Retorna un número aleatorio del 1 al 100 con el módulo random

def comprobar_numero():              #Se crea la función para comprobar si el intento del usuario es igual al número secreto
    try:                                                                         
        numero_intentado=int(Entrada_intento.get().strip())            #Se obtiene la entrada del usuario y se eliminan espacios en blanco
    except ValueError:                                                  #Manejo de error en caso de que el usuario no ingrese un número válido               
        etiqueta_resultado2.config(text="Digita un número válido.")      #Se genera el resultado y se cambia la etiqueta       
        return                                                                  #Retorno para volver a ingresar un número
    if numero_intentado < 1 or numero_intentado > 100:                             #Condicional si el intento es fuera del rango solicitado
        etiqueta_resultado2.config(text="Digita un número dentro del rango.")          #Se genera el resultado y se cambia la etiqueta   
    elif numero_intentado > numero_secreto:                                            #Condicional si el intento del usuario es mayor que el número secreto
        etiqueta_resultado2.config(text="Intenta un número más bajo.")             #Se genera el resultado y se cambia la etiqueta   
        sumar_intento()                                                            #Se lleva a cabo la función de sumar intento para que se refleje en la etiqueta de intentos
    elif numero_intentado < numero_secreto:                                     #Condicional si el intento del usuario es menor que el número secreto
        etiqueta_resultado2.config(text="Intenta un número más alto.")             #Se genera el resultado y se cambia la etiqueta   
        sumar_intento()                                                            #Se lleva a cabo la función de sumar intento para que se refleje en la etiqueta de intentos
    else:                                                                                                        #Condicional si el intento del usuario es igual al número secreto
        etiqueta_resultado2.config(text="¡Correcto! Adivinaste el número secreto: "+ str(numero_secreto))        #Se genera el resultado y se cambia la etiqueta   
        sumar_intento()
        boton_comprobar.config(state="disabled")                      #Se bloquea el botón comprobar para dar a entender que el juego terminó
        ventana.unbind("<Return>")                           #Se desenlaza el botón comprobar con la tecla "Enter"
    Entrada_intento.delete(0, tk.END)                 #Se borra la entrada del usuario para ingresar el próximo intento
    
    

def sumar_intento():                                       #Se crea la función para sumar los intentos a medida que el usuario trata de adivinar
    intentos = int(etiqueta_intentos2.cget("text"))               #Se toma el valor que hay en la etiqueta de intentos
    intentos += 1                                       #Se suma un intento
    etiqueta_intentos2.config(text=intentos)                 #Se edita la etiqueta de intentos

def nueva_partida():                                                # Función para comenzar una nueva partida
    ventana.bind("<Return>", lambda event: comprobar_numero())     # Asocia la tecla Enter con la función comprobar_numero
    global numero_secreto                                           # Declara la variable numero_secreto como global
    numero_secreto = generar_numero()                               # Genera un nuevo número secreto
    etiqueta_resultado2.config(text="")                             # Limpia el mensaje de resultado anterior
    etiqueta_intentos2.config(text="0")                             # Reinicia el contador de intentos
    Entrada_intento.delete(0, tk.END)                               # Limpia el campo de entrada
    boton_comprobar.config(state="normal")                          # Activa el botón de comprobar nuevamente

def iniciar_juego():                                                # Función que inicia el juego desde la pantalla de inicio
    mostrar_pantalla(pantalla_juego)                                # Muestra la pantalla del juego
    nueva_partida()                                                 # Llama a nueva_partida para reiniciar el juego

def mostrar_pantalla(pantalla):                                     # Función para mostrar una pantalla y ocultar las otras
    for f in (pantalla_inicio, pantalla_juego):                     # Recorre todas las pantallas
        f.pack_forget()                                             # Oculta cada pantalla
    pantalla.pack(fill="both", expand=True)                         # Muestra la pantalla solicitada

def salir():                                                        # Función para volver a la pantalla de inicio
    mostrar_pantalla(pantalla_inicio)                               # Muestra la pantalla de inicio

#=========================================
# CONFIGURACIÓN DE LA VENTANA
#=========================================
ventana = tk.Tk()                                                   # Crea una nueva ventana principal
ventana.title("Adivina el Número")                                  # Asigna un título a la ventana
ventana.geometry("600x250")                                         # Define el tamaño de la ventana

#=========================================
# PANTALLA DE INICIO
#=========================================
pantalla_inicio = tk.Frame(ventana)                                 # Crea el frame de la pantalla de inicio

pantalla_inicio.columnconfigure(0, weight=1)                         # Configura columnas para centrar contenido
pantalla_inicio.columnconfigure(1, weight=1)
pantalla_inicio.columnconfigure(2, weight=1)

tk.Label(pantalla_inicio, text="").grid(row=0, column=0)            # Espacio en blanco para estética

etiqueta_titulo = tk.Label(pantalla_inicio, text="¡Bienvenido a Adivina el Número!", font=("Courier New", 14))  # Título del juego
etiqueta_titulo.grid(row=1, column=0, columnspan=3, sticky="we")    # Ubica el título centrado

tk.Label(pantalla_inicio, text="").grid(row=2, column=0)            # Espacios en blanco para separar elementos
tk.Label(pantalla_inicio, text="").grid(row=3, column=0)
tk.Label(pantalla_inicio, text="").grid(row=4, column=0)

boton_iniciar_juego = tk.Button(pantalla_inicio, text="Iniciar Juego", command=iniciar_juego, font=("Courier New", 11))  # Botón de iniciar juego
boton_iniciar_juego.grid(row=5, column=1)                           # Posiciona el botón en el centro

#=========================================
# PANTALLA DEL JUEGO
#=========================================
pantalla_juego = tk.Frame(ventana)                                  # Crea el frame de la pantalla del juego

pantalla_juego.columnconfigure(0, weight=1)                         # Configura columnas
pantalla_juego.columnconfigure(1, weight=1)
pantalla_juego.columnconfigure(2, weight=1)

etiqueta_titulo = tk.Label(pantalla_juego, text="Adivina el Número", font=("Courier New", 12))  # Título de la pantalla de juego
etiqueta_titulo.grid(row=0, column=0, columnspan=3, sticky="we")

etiqueta_instrucciones1 = tk.Label(pantalla_juego, text="Instrucciones: Intenta adivinar el número secreto entre 1 y 100.", font=("Courier New", 10))
etiqueta_instrucciones1.grid(row=2, column=0, columnspan=3, sticky="we")  # Instrucciones del juego

tk.Label(pantalla_juego, text="").grid(row=3, column=0)            # Espacio en blanco

etiqueta_tu_intento = tk.Label(pantalla_juego, text="  Tu intento:", font=("Courier New", 10))  # Etiqueta para campo de entrada
etiqueta_tu_intento.grid(row=4, column=0)

Entrada_intento = tk.Entry(pantalla_juego, justify="center")       # Campo de entrada para que el usuario digite su número
Entrada_intento.grid(row=4, column=1)

boton_comprobar = tk.Button(pantalla_juego, text="Comprobar", command=comprobar_numero, font=("Courier New", 10))  # Botón para comprobar el número ingresado
boton_comprobar.grid(row=4, column=2)

etiqueta_resultado1 = tk.Label(pantalla_juego, text="  Resultado:", font=("Courier New", 10))  # Etiqueta del resultado
etiqueta_resultado1.grid(row=5, column=0)

etiqueta_resultado2 = tk.Label(pantalla_juego, text="", font=("Courier New", 10))              # Resultado del intento (dinámico)
etiqueta_resultado2.grid(row=5, column=1)

etiqueta_intentos = tk.Label(pantalla_juego, text="  Intentos:", font=("Courier New", 10))     # Etiqueta para número de intentos
etiqueta_intentos.grid(row=6, column=0)

etiqueta_intentos2 = tk.Label(pantalla_juego, text="0", font=("Courier New", 10))              # Contador de intentos
etiqueta_intentos2.grid(row=6, column=1)

boton_nueva_partida = tk.Button(pantalla_juego, text="Nueva Partida", command=nueva_partida, font=("Courier New", 10))  # Botón para reiniciar el juego
boton_nueva_partida.grid(row=7, column=1)

tk.Label(pantalla_juego, text="").grid(row=8, column=0)            # Espacio en blanco

boton_salir = tk.Button(pantalla_juego, text="Salir", command=salir, font=("Courier New", 10))  # Botón para salir a la pantalla de inicio
boton_salir.grid(row=9, column=1)

ventana.bind("<Return>", lambda event: comprobar_numero())         # Asocia la tecla Enter con la función de comprobar el número

#=========================================
# GENERAR PROGRAMA
#=========================================
numero_secreto = generar_numero()                                   # Genera un número secreto al iniciar el programa
mostrar_pantalla(pantalla_inicio)                                   # Muestra la pantalla de inicio al comenzar

ventana.mainloop()                                                  # Inicia el bucle principal de la ventana (ejecución del programa)