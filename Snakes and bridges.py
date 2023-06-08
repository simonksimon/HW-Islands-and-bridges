import tkinter as tk
import random
pw=50
ph=50
countwidth=random.randrange(4,7)
countheight=random.randrange(3,10)
win=tk.Tk()
canvas=tk.Canvas(width=countwidth*pw+200,height=countheight*ph,bg="grey")
canvas.pack()
water=[]
islands=[]
img=tk.PhotoImage(file="ostrov3.png")
img1=tk.PhotoImage(file="ostrov0.png")
img2=tk.PhotoImage(file="ostrov1.png")
img3=tk.PhotoImage(file="ostrov2.png")
img4=tk.PhotoImage(file="ostrov_kruh0.png")
img5=tk.PhotoImage(file="ostrov_kruh1.png")
switchero=[]
text = []
penazenka = 0
def zmenar(e):
    global water,penazenka
    print("I klikd.")
    zoz=canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if len(zoz)!=0 and zoz[0] in water:
        print("You klikd on vodu.")
        nx=(e.x//pw)*pw
        ny=(e.y//ph)*ph
        temp=zoz[0]
        canvas.delete(temp)
        water.remove(temp)
        if canvas.itemcget(switchero[0],'image')=='pyimage5':
            canvas.create_image(nx,ny,anchor="nw",image=img2,tag="most")
            penazenka += 10
            canvas.itemconfig(text[0], text=penazenka)
        elif canvas.itemcget(switchero[0],'image')=='pyimage6':
            canvas.create_image(nx, ny, anchor="nw", image=img1)
            penazenka += 50
            canvas.itemconfig(text[0], text=penazenka)
def otáčač(e):
    zoz = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    print(canvas.itemcget(zoz[0],"image"))
    if canvas.itemcget(zoz[0],'image')=='pyimage4':
        canvas.itemconfig(zoz[0],image=img2)
    else:
        canvas.itemconfig(zoz[0],image=img3)

def setup():
    global water,islands,countwidth
    for y in range(countheight):
        for x in range(countwidth):
            result=random.random()
            if result>=0.2:
                #img=tk.PhotoImage(file="image/ostrov3.png")
                water.append(canvas.create_image(pw*x,ph*y,anchor="nw",image=img))
            else:
                #img=tk.PhotoImage(file="image/ostrov0.png")
                islands.append(canvas.create_image(pw * x, ph * y, anchor="nw", image=img1))
    switchero.append(canvas.create_image(pw*countwidth+100,0,anchor="nw",image=img4,tag="zmena"))
    text.append(canvas.create_text(countwidth * pw + 100, 80, text=penazenka))
def switcheroo(e):
    overlap = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if canvas.itemcget(overlap[0],'image')=='pyimage5':
        canvas.itemconfig(overlap[0],image=img5)
    else:
        canvas.itemconfig(overlap[0],image=img4)

canvas.bind("<Button-1>",zmenar)
canvas.tag_bind("most","<Button-1>",otáčač)
canvas.tag_bind('zmena','<Button-1>',switcheroo)
setup()
win.mainloop()