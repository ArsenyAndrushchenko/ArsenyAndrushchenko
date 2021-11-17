from tkinter import *
from tkinter import messagebox
# Ниже представленны переменные, которые будут использоваться в будующем. Пока что они не используються
W, H = 10, 20
TILE = 45
GAME_RES = W * TILE, H * TILE
RES = 800, 930 # Изначально 750, 940. Былоо увеличино для большего рабочего места
FPS = 60


def on_closing():
    #if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        tk.destroy()



tk = Tk()
tk.protocol("WM_DELETE_WINDOW", on_closing) # Обработка функции on_closing при закрытии окна
tk.title("Тетрис РГГМУ") # Название окна
tk.resizable(0, 0) # Эта функция позмоляет маштабировать окно (Она практически бесполезна, весть картинку в окне масштабировать не получитья)
tk.wm_attributes("-topmost", 1)
#tk.iconbitmap("Icons/icon image for tetris")

canvas = Canvas(tk, width=RES[0], height=RES[1], bg="black", highlightthickness=0) #Задний фон (черный)
canvas.pack()

img_obj2 = PhotoImage(file="Icons/bg2.png")
canvas.create_image(20, 20, anchor=NW, image=img_obj2)

grid = [canvas.create_rectangle(x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE) for x in range(W) for y in range(H)]
for item in grid:
    canvas.move(item, 20, 20)


#canvas.create_oval(100, 100, 300, 300, fill="yellow", outline="")
#canvas.create_oval(120, 120, 280, 280, fill="white", outline="")

#canvas.create_rectangle(400,100,500,500, fill="lightgreen")
#canvas.create_rectangle(420,120,480,480, fill="darkgreen", outline="")

canvas.create_text(625, 60,text="Тетрис РГГМУ", font=("Arial", 30),fill="white")


tk.mainloop()