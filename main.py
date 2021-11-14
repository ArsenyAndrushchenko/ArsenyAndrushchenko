from tkinter import *
from tkinter import messagebox

W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
RES = 750, 940
FPS = 60


def on_closing():
    #if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()



tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing)
tk.title("Тетрис РГГМУ")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
#tk.iconbitmap("Icons/icon image for tetris")

canvas = Canvas(tk, width=RES[0], height=RES[1], bg="black", highlightthickness=0)
canvas.pack()

img_obj2 = PhotoImage(file="Icons/bg2.png")
canvas.create_image(20, 20, anchor=NW, image=img_obj2)

#canvas.create_oval(100, 100, 300, 300, fill="yellow", outline="")
#canvas.create_oval(120, 120, 280, 280, fill="white", outline="")

#canvas.create_rectangle(400,100,500,500, fill="lightgreen")
#canvas.create_rectangle(420,120,480,480, fill="darkgreen", outline="")

#canvas.create_text(200,500,text="Hello World!", font=("Arial", 40),fill="white")


tk.mainloop()