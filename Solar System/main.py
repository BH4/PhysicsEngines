import Tkinter
from classes import particle,solar

h=700
w=1200



root = Tkinter.Tk()
canvas = Tkinter.Canvas(root, bg="white", height=h, width=w)
system=solar(canvas)
system.randPopulate(100,300)
#system.populateOrbit()

def loop():
    dispTime=.5
    dt=1e-10

    system.force(dispTime,dt)




    root.after(1,loop)
    












root.after(0,loop)

canvas.pack()
root.mainloop()
