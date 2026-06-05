import tkinter as tk

# ==========================
# VENTANA
# ==========================

ventana = tk.Tk()
ventana.title("Evaluador Inteligente")
ventana.geometry("900x600")
ventana.configure(bg="black")

# ==========================
# CANVAS
# ==========================

canvas = tk.Canvas(
    ventana,
    width=900,
    height=600,
    bg="black",
    highlightthickness=0
)

canvas.pack()

# ==========================
# RELOJ MINIMALISTA
# ==========================

# Círculo exterior azul
canvas.create_oval(
    250, 50, 650, 450,
    outline="#306998",
    width=12
)

# Círculo interior amarillo
canvas.create_oval(
    280, 80, 620, 420,
    outline="#FFD43B",
    width=4
)

# Manecillas decorativas
canvas.create_line(
    450, 250,
    450, 140,
    fill="#FFD43B",
    width=8
)

canvas.create_line(
    450, 250,
    540, 310,
    fill="#306998",
    width=8
)

# Centro
canvas.create_oval(
    435, 235, 465, 265,
    fill="#FFD43B",
    outline="#FFD43B"
)

# ==========================
# TEXTO
# ==========================

canvas.create_text(
    450,
    520,
    text="EVALUADOR INTELIGENTE\nDE ADMINISTRACIÓN DE TIEMPO",
    fill="#FFD43B",
    font=("Arial", 24, "bold"),
    justify="center"
)

ventana.mainloop()