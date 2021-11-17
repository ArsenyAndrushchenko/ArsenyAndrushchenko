from tkinter import *
#from tkinter import massagebox
from random import choice, randrange
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


canvas = Canvas(tk, width=RES[0], height=RES[1], bg="black", highlightthickness=0) #Задний фон (черный)
canvas.pack()

img_obj2 = PhotoImage(file="Icons/bg2.png")
canvas.create_image(20, 20, anchor=NW, image=img_obj2)

grid = [canvas.create_rectangle(x * TILE, y * TILE, x * TILE+TILE, y * TILE+TILE) for x in range(W) for y in range(H)]
for item in grid:
    canvas.move(item, 20, 20)

score = 0
record = "0"

canvas.create_text(535, 780,text="score:", font=("Arial", 30),fill="white", anchor=NW) #Отрисовка текста и счета
canvas.create_text(550, 840,text=str(score), font=("Arial", 30),fill="white", anchor=NW)
canvas.create_text(525, 650,text="record:", font=("Arial", 30),fill="gold", anchor=NW)
canvas.create_text(550, 710,text=record, font=("Arial", 30),fill="gold", anchor=NW)
canvas.create_text(625, 60,text="Tetris RSHU", font=("Arial", 30),fill="white")

get_color = lambda : (randrange(30, 256), randrange(30, 256), randrange(30, 256))

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

#print(rgb_to_hex(get_color()))

for item in grid:
    canvas.itemconfigure(item, fill=rgb_to_hex(get_color()))

#for item in grid:
#    canvas.itemconfigure(item, fill="")

tk.mainloop()