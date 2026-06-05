# ==========================================
# PROYECTO FINAL PYTHON
# LOGIN + MENU + REGISTRO + REPORTES
# ==========================================

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
import os
import sqlite3

conexion = sqlite3.connect("actividades.db")
cursor = conexion.cursor()

# ==========================================
# USUARIOS
# ==========================================

usuarios = {
    "Jorge": "cbtasub",
    "Ulises": "cbtasub",
    "Fernando": "cbtasub"
}

# ==========================================
# ARREGLOS
# ==========================================

actividades = []
dias = []
horas = []

# ==========================================
# REGISTRO DE ACTIVIDADES
# ==========================================

def ventana_registro():

    registro = tk.Toplevel()
    registro.title("Registro de Actividades")
    registro.geometry("700x500")
    registro.configure(bg="#FFD43B")

    tk.Label(
        registro,
        text="Registro de Actividades",
        font=("Arial", 20, "bold"),
        bg="#FFD43B"
    ).pack(pady=20)

    tk.Label(
        registro,
        text="Actividad",
        bg="#FFD43B"
    ).pack()

    entry_actividad = tk.Entry(registro, width=40)
    entry_actividad.pack(pady=5)

    tk.Label(
        registro,
        text="Día",
        bg="#FFD43B"
    ).pack()

    entry_dia = tk.Entry(registro, width=40)
    entry_dia.pack(pady=5)

    tk.Label(
        registro,
        text="Horas",
        bg="#FFD43B"
    ).pack()

    entry_horas = tk.Entry(registro, width=40)
    entry_horas.pack(pady=5)

    def guardar():

        actividad = entry_actividad.get().strip()
        dia = entry_dia.get().strip()

        try:

            h = float(entry_horas.get())

            if actividad == "" or dia == "":
                messagebox.showerror(
                    "Error",
                    "Todos los campos son obligatorios"
                )
                return

            actividades.append(actividad)
            dias.append(dia)
            horas.append(h)

            messagebox.showinfo(
                "Guardado",
                "Actividad registrada correctamente"
            )

            entry_actividad.delete(0, tk.END)
            entry_dia.delete(0, tk.END)
            entry_horas.delete(0, tk.END)

        except:
            messagebox.showerror(
                "Error",
                "Las horas deben ser numéricas"
            )

    tk.Button(
        registro,
        text="Guardar Actividad",
        bg="green",
        fg="white",
        font=("Arial", 12, "bold"),
        command=guardar
    ).pack(pady=20)

# ==========================================
# REPORTES
# ==========================================

def ventana_reportes():

    reportes = tk.Toplevel()
    reportes.title("Reportes")
    reportes.geometry("850x550")

    texto = tk.Text(reportes, width=95, height=30)
    texto.pack(pady=20)

    texto.insert(tk.END, "===== REPORTE GENERAL =====\n\n")

    total = 0

    for i in range(len(actividades)):

        texto.insert(
            tk.END,
            f"Actividad: {actividades[i]} | Día: {dias[i]} | Horas: {horas[i]}\n"
        )

        total += horas[i]

    texto.insert(tk.END, "\n")

    texto.insert(
        tk.END,
        f"TOTAL DE HORAS: {total}\n"
    )

    if len(horas) > 0:

        promedio = total / len(horas)

        texto.insert(
            tk.END,
            f"PROMEDIO: {round(promedio,2)} horas\n"
        )
    else:
        texto.insert(
            tk.END,
            "PROMEDIO: 0 horas\n"
        )

# ==========================================
# GRAFICA
# ==========================================

def grafico():

    try:

        if len(actividades) == 0:

            messagebox.showwarning(
                "Sin datos",
                "No hay actividades registradas."
            )

            return

        plt.figure(figsize=(8,5))

        plt.bar(
            actividades,
            horas
        )

        plt.title(
            "Administración del Tiempo"
        )

        plt.xlabel(
            "Actividades"
        )

        plt.ylabel(
            "Horas"
        )

        plt.grid(axis="y")

        plt.show()

    except Exception as e:

        messagebox.showerror(
            "Error",
            f"No se pudo generar la gráfica\n{e}"
        )

# ==========================================
# MENU PRINCIPAL
# ==========================================

def abrir_menu(usuario):

    menu = tk.Toplevel()

    menu.title("Menú Principal")
    menu.geometry("800x600")
    menu.configure(bg="#306998")

    tk.Label(
        menu,
        text=f"Bienvenido {usuario}",
        font=("Arial", 24, "bold"),
        bg="#306998",
        fg="white"
    ).pack(pady=30)

    tk.Button(
        menu,
        text="Registrar Actividades",
        font=("Arial", 14, "bold"),
        width=25,
        command=ventana_registro
    ).pack(pady=15)

    tk.Button(
        menu,
        text="Ver Reportes",
        font=("Arial", 14, "bold"),
        width=25,
        command=ventana_reportes
    ).pack(pady=15)

    tk.Button(
        menu,
        text="Mostrar Gráfica",
        font=("Arial", 14, "bold"),
        width=25,
        command=grafico
    ).pack(pady=15)

    tk.Button(
        menu,
        text="Salir",
        font=("Arial", 14, "bold"),
        width=25,
        bg="red",
        fg="white",
        command=menu.destroy
    ).pack(pady=15)

# ==========================================
# LOGIN
# ==========================================

def validar_login():

    usuario = entrada_usuario.get().strip()
    password = entrada_password.get().strip()

    if usuario in usuarios and usuarios[usuario] == password:

        messagebox.showinfo(
            "Acceso Correcto",
            f"Bienvenido {usuario}"
        )

        abrir_menu(usuario)

    else:

        messagebox.showerror(
            "Error",
            "Usuario o contraseña incorrectos"
        )

# ==========================================
# SALIR
# ==========================================

def salir():
    ventana.destroy()

# ==========================================
# VENTANA LOGIN
# ==========================================

ventana = tk.Tk()

ventana.title("Sistema Inteligente de Administración de Tiempo")
ventana.geometry("1000x650")
ventana.configure(bg="#306998")
ventana.resizable(False, False)

# ==========================================
# TITULO
# ==========================================

titulo = tk.Label(
    ventana,
    text="Sistema Inteligente de Administración de Tiempo",
    font=("Arial", 24, "bold"),
    bg="#306998",
    fg="white"
)

titulo.pack(pady=30)

# ==========================================
# FRAME LOGIN
# ==========================================

frame_login = tk.Frame(
    ventana,
    bg="#FFD43B",
    bd=3,
    relief="ridge"
)

frame_login.place(
    x=250,
    y=170,
    width=500,
    height=300
)

# ==========================================
# USUARIO
# ==========================================

lbl_usuario = tk.Label(
    frame_login,
    text="Usuario:",
    font=("Arial", 14, "bold"),
    bg="#FFD43B"
)

lbl_usuario.place(x=50, y=60)

entrada_usuario = tk.Entry(
    frame_login,
    font=("Arial", 14),
    width=25
)

entrada_usuario.place(x=170, y=60)

# ==========================================
# CONTRASEÑA
# ==========================================

lbl_password = tk.Label(
    frame_login,
    text="Contraseña:",
    font=("Arial", 14, "bold"),
    bg="#FFD43B"
)

lbl_password.place(x=50, y=130)

entrada_password = tk.Entry(
    frame_login,
    font=("Arial", 14),
    width=25,
    show="*"
)

entrada_password.place(x=170, y=130)

# ==========================================
# BOTONES
# ==========================================

btn_ingresar = tk.Button(
    frame_login,
    text="Ingresar",
    font=("Arial", 12, "bold"),
    bg="#306998",
    fg="white",
    width=15,
    command=validar_login
)

btn_ingresar.place(x=80, y=220)

btn_salir = tk.Button(
    frame_login,
    text="Salir",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    width=15,
    command=salir
)

btn_salir.place(x=270, y=220)

# ==========================================
# MAIN
# ==========================================

ventana.mainloop()