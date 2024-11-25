import tkinter as tk
from tkinter import Menu

# Crear la ventana principal
root = tk.Tk()
root.title("Ventana Completa")

# Configurar el color de fondo
root.configure(bg='white')

# Crear un lienzo para dibujar las rayas verdes
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

# Dibujar las rayas verdes
#for i in range(0, root.winfo_screenwidth(), 20):#
#    canvas.create_line([(i, 0), (i, root.winfo_screenheight())], fill='green', width=2)##

# Crear el botón 'menu' en la esquina inferior izquierda
menu_button = tk.Button(root, text="Menu", bg='green', fg='white')
menu_button.place(relx=0, rely=1, anchor='sw')

# Crear el botón 'característica' en la esquina superior derecha
caracteristica_button = tk.Menubutton(root, text="Característica", bg='green', fg='white')
caracteristica_button.menu = Menu(caracteristica_button, tearoff=0)
caracteristica_button["menu"] = caracteristica_button.menu

# Añadir opciones al menú 'característica'
caracteristica_button.menu.add_command(label="Sonido")
caracteristica_button.menu.add_command(label="Característica")
caracteristica_button.menu.add_command(label="Sor Lenor")
caracteristica_button.menu.add_command(label="Como Jugar")
caracteristica_button.menu.add_command(label="Registrar")

caracteristica_button.place(relx=1, rely=0, anchor='ne')

# Función para crear sub-menú para el botón 'menu'
def create_sub_menu():
    sub_menu = tk.Menu(menu_button, tearoff=0)
    sub_menu.add_command(label="Global")
    sub_menu.add_command(label="Grupal")
    sub_menu.add_command(label="Avatar")
    sub_menu.add_command(label="Dictado")
    sub_menu.add_command(label="Carrera")
    return sub_menu

# Vincular el sub-menú al botón 'menu'
menu_button.bind("<Button-1>", lambda event: create_sub_menu().post(event.x_root, event.y_root))

# Crear botones para cerrar, maximizar y minimizar la ventana
close_button = tk.Button(root, text="Cerrar", command=root.destroy, bg='red', fg='white')
close_button.place(relx=1, rely=1, anchor='se')

maximize_button = tk.Button(root, text="Maximizar", command=lambda: root.state('zoomed'), bg='blue', fg='white')
maximize_button.place(relx=0.9, rely=1, anchor='se')

minimize_button = tk.Button(root, text="Minimizar", command=lambda: root.iconify(), bg='yellow', fg='black')
minimize_button.place(relx=0.8, rely=1, anchor='se')

# Iniciar el bucle principal
root.mainloop()