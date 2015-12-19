import math
from vector import vector

#with this implementation, any quantity assosiated with the particle must
#remain constant except the position and velocity. If a differential equation
#for another quantitiy is to be  added then it must be passed along with
#posN and velN to acceleration

def RK4(particleList,Id,t,dt,a,files):#uses Runge-Kutta method (currently 4th order) to evaluate the next value in the iteration of x
    #assumes functString uses x and t as its only arguments
    #this function will have to import functions differently depending on what is called in functString
    t=float(t)
    dt=float(dt)

    zero=vector()
    
    [Id,particle]=particleList.get(Id)
    pos=particle.getPos()
    vel=particle.getVel()
    
    k1=evaluate(particleList,Id,t,0,a,files,zero,zero)
    k2=evaluate(particleList,Id,t,dt*.5,a,files,k1[0],k1[1])
    k3=evaluate(particleList,Id,t,dt*.5,a,files,k2[0],k2[1])
    k4=evaluate(particleList,Id,t,dt,a,files,k3[0],k3[1])

    newPos=pos+(k1[0]+k2[0]*2+k3[0]*2+k4[0])*(dt/6)
    newVel=vel+(k1[1]+k2[1]*2+k3[1]*2+k4[1])*(dt/6)
    t=t+dt

    return [newPos,newVel,t]


def evaluate(particleList,Id,t,dt,a,files,posD,velD):
    [Id,particle]=particleList.get(Id)
    pos=particle.getPos()
    vel=particle.getVel()
    
    posN=pos+posD*dt
    velN=vel+velD*dt

    outPosD=velN
    outVelD=acceleration(posN,velN,particleList,Id,t+dt,a,files)
    return [outPosD,outVelD]

def acceleration(pos,vel,particleList,Id,t,a,files):
    #given list of functions
    tot=vector(x=0,y=0,z=0)
    for i,func in enumerate(a):
        tot=tot+func(pos,vel,particleList,Id,t,files[i])

    return tot
