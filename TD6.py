from tkinter import *
from random import random
import numpy as np
root = Tk()

#EXERCICE 1

w = 400
h = 400
root.title('graphs')
root.geometry("400x400")

can = Canvas(root, width = 400, height = 400, bg = 'white')
can.grid(row = 0, column = 0)

graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0],
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]


pos = np.array([(random()*w, random()*h)for i in range(len(graph))])

def draw(can, graph, pos):
    k = 0
    for i in range(len(graph)):
        for j in graph[i]:
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-8,y-8,x+8,y+8,fill="#f3e1d4")
        can.create_text(x,y, text=f"{k}", font = ("Times", "8", "bold"), fill = "black")
        k = k + 1

#EXERCICE 2

tau = 0.1
l0 = 100
k = 1
draw(can, graph, pos)

def ressort(can, graph, pos):
    vit = np.array([((random()-0.5)*10, (random()-0.5)*10)for i in range(len(graph))])
    for i in range (len(graph)):
        for x in graph[i]:
            norm_ix = np.sqrt((pos[i][0] - pos[x][0])**2 + (pos[i][1] - pos[x][1])**2)
            unit = np.array([(pos[i][0] - pos[x][0])/ norm_ix , (pos[i][1] - pos[x][1])/norm_ix])
            F_vect = -k*(norm_ix - l0) * unit
            vit[i] = vit[i] + tau*F_vect
            pos[i][0] = pos[i][0] + tau*vit[i][0]
            pos[i][1] = pos[i][1] + tau*vit[i][1]
    return pos

def redraw(can, graph, pos):
    k = 0
    can.delete("all")
    posi = ressort(can, graph, pos)
    for i in range(len(graph)):
        for j in graph[i]:
            can.create_line(posi[i][0], posi[i][1], posi[j][0], posi[j][1])
    for (x, y) in posi:
        can.create_oval(x-8,y-8,x+8,y+8,fill="#f3e1d4")
        can.create_text(x,y, text=f"{k}", font = ("Times", "8", "bold"), fill = "black")
        k = k + 1


root.bind("<f>", lambda e : redraw(can,graph,pos))
root.mainloop()
