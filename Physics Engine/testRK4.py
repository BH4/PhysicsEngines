#test RK4
from RungeKutta import RK4
from vector import vector
from kicks import *
from particleList import particleList

l=particleList()
l.add(particle(nq=-3.05834e19))

t=0
dt=.001

a=[EarthG,constEfeild]
files=[None,None]


while t<1:
    Id=l.nextId(-1)
    while not(Id is None):
        move(l,Id,t,dt,a,files)
        Id=l.nextId(Id)

    t=t+dt

Id=l.nextId(-1)
[Id,particle]=l.get(Id)
pos=particle.getPos()
vel=particle.getVel()

print vel.y,pos.y
