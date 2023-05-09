import tkinter as tk
# from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
# from scipy import integrate

root = tk.Tk()
root.title('Hola mundo! es mi primera prueba')
# root.Iconbitmap('dirección')
root.geometry()


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.figure()
    plt.hist(house_prices, 50)
    plt.show()


tk.my_buttom = tk.Button(root, text = 'Graph it!', command = graph)
tk.my_buttom.pack()

root.mainloop()
