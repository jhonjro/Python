import tkinter as tk

# ventana
ventana = tk.Tk()
ventana.geometry("400x300")

# Etiqueta
etiqueta = tk.Label(ventana, text='Calculo de costos por viaje')
etiqueta.pack()

# Caja numero de personas
etiqueta_1 = tk.Label(ventana, text='Número de personas')
etiqueta_1.pack()
numero_personas = tk.Entry(ventana)
numero_personas.pack()

# Caja km recorrido
etiqueta_2 = tk.Label(ventana, text='Kilometros recorridos')
etiqueta_2.pack()
km_recorrido = tk.Entry(ventana)
km_recorrido.pack()

# Caja tipo de bus
etiqueta_2 = tk.Label(ventana, text='Tipo de bus')
etiqueta_2.pack()
tipo_bus = tk.Entry(ventana, )
tipo_bus.pack()

# funcion calcular total


def calcular_total():
    if numero_personas.get() and km_recorrido.get() and tipo_bus.get():
        if int(numero_personas.get()) >= 20:
            if tipo_bus.get().lower() == 'a':
                print('El costo total es: ', 2*float(numero_personas.get())*float(km_recorrido.get()))
            elif tipo_bus.get().lower() == 'b':
                print('El costo total es: ', 2.5*float(numero_personas.get())*float(km_recorrido.get()))
            elif tipo_bus.get().lower() == 'c':
                print('El costo total es: ', 3*float(numero_personas.get())*float(km_recorrido.get()))
            else:
                print('No existe este tipo de bus')
        else:
            print('Este bus aún no puede partir')
    else:
        print('Ingrese información restante!')


# funcion calcular total


def calcular_persona():
    if numero_personas.get() and km_recorrido.get() and tipo_bus.get():
        if int(numero_personas.get()) >= 20:
            if tipo_bus.get().lower() == 'a':
                print('El costo por persona es: ', 2*float(km_recorrido.get()))
            elif tipo_bus.get().lower() == 'b':
                print('El costo por persona es: ', 2.5*float(km_recorrido.get()))
            elif tipo_bus.get().lower() == 'c':
                print('El costo por persona es: ', 3*float(km_recorrido.get()))
            else:
                print('No existe este tipo de bus')
        else:
            print('Este bus aún no puede partir')
    else:
        print('Ingrese información restante!')


# Boton para calcular costos total
boton_calcular_total = tk.Button(ventana, text='Calcular total', command=calcular_total)
boton_calcular_total.pack()

# Boton para calcular costos persona
boton_calcular_persona = tk.Button(ventana, text='Calcular por persona', command=calcular_persona)
boton_calcular_persona.pack()


ventana.mainloop()


# tipo_bus
# numero_personas
# km_recorrido
