from random import random
import numpy as np
import scipy as sp
import scipy.integrate
import warnings

def rand(low,high):
    return random()*(high-low)+low

def polarToCart(r,theta):
    x=r*np.cos(theta)
    y=r*np.sin(theta)
    return [x,y]

def cartToPolar(x,y):
    r=np.sqrt(x**2+y**2)

    if x<0:
        theta=np.arctan(y/x)+np.pi
    elif x==0 and y>0:
        theta=np.pi/2
    elif x==0 and y>0:
        theta=3*np.pi/2
    elif y<0:
        theta=np.arctan(y/x)+2*np.pi
    else:
        theta=np.arctan(y/x)
        
    
    return [r,theta]

'''
def integrate(F,tmax,dt,x0,y0,dx0,dy0,t0):
    r=spint.ode(F).set_integrator('dopri5', atol=1e-10, rtol=1e-10)
    r.set_initial_value([x0,y0,dx0,dy0],t0)
    while (r.successful() and r.t-t0<tmax):
        val=r.integrate(r.t+dt)
        newt=r.t

    return [newt,val]
'''

def integrate_ode(f, initial, t0, tfinal, tol=1e-6):
    tlist = []
    ylist = []
    solver = sp.integrate.ode(f)
    solver.set_integrator('vode', rtol=tol, atol=tol*1e-3)
    solver.set_initial_value(initial, t0)
    warnings.filterwarnings("ignore", category=UserWarning)
    while solver.t < tfinal:
        if not solver.successful():
            print 'Failed'
            break
        solver.integrate(tfinal, step=True)
        tlist.append(solver.t)
        ylist.append(solver.y)
    warnings.resetwarnings()
    return np.array(tlist), np.array(ylist)

class particle:
    G=10
    
    def __init__(self,canvas,mass,x,y,dx,dy):
        #intrinsic
        self.rad=mass
        self.m=mass

        #position
        self.x=x
        self.y=y

        #velocity
        self.dx=dx
        self.dy=dy

        #drawing stuff
        self.canvas=canvas
        
        w=int(self.canvas.cget("width"))
        h=int(self.canvas.cget("height"))
        self.offx=w/2.
        self.offy=h/2.

        self.color='black'
        self.id=self.canvas.create_oval((self.x+self.offx-self.rad,self.y+self.offy-self.rad,self.x+self.offx+self.rad,self.y+self.offy+self.rad),fill=self.color)

    def __eq__(self,other):
        return self.__dict__==other.__dict__

    def refreshPic(self):
        
        self.canvas.coords(self.id,(self.x+self.offx-self.rad,self.y+self.offy-self.rad,self.x+self.offx+self.rad,self.y+self.offy+self.rad))

    def gravF(self,other):
        
        if self==other:
            return [0,0]

        [r,theta]=cartToPolar(other.x,other.y)
        f=particle.G*self.m*other.m/(self.dis(other))**2
        fx=f*np.cos(theta)
        fy=f*np.sin(theta)
        return [fx,fy]

    def dis(self,other):
        delx=self.x-other.x
        dely=self.y-other.y

        return np.sqrt(delx**2+dely**2)
    
    

class solar:
    def __init__(self,canvas):
        self.particles=[]
        self.canvas=canvas
        self.time=0

    def randPopulate(self,num,rad):
        #w=int(self.canvas.cget("width"))
        #h=int(self.canvas.cget("height"))
        #offx=w/2.
        #offy=h/2.
        maxMass=2
        minMass=1
        minVel=-3
        maxVel=3

        for i in xrange(num):
            r=rand(0,rad)
            theta=rand(0,2*np.pi)
            [x,y]=polarToCart(r,theta)
            #x+=offx
            #y+=offy
            self.particles.append(particle(self.canvas,rand(minMass,maxMass),x,y,rand(minVel,maxVel),rand(minVel,maxVel)))


    def populateOrbit(self):
        p1=particle(self.canvas,5.,20.,0.,0.,1.)
        p2=particle(self.canvas,5.,-20.,0.,0.,-1.)
        self.particles=[p1,p2]

    def force(self,timeChange,dt):
        
        for p in self.particles:
            fxtot=0
            fytot=0
            for po in self.particles:
                [fx,fy]=p.gravF(po)
                fxtot+=fx
                fytot+=fy


            #Y=[x,y,dx,dy]
            #F=[dx,dy,ddx,ddy]
            F=lambda t,Y: np.array([Y[2],Y[3],fxtot/p.m,fytot/p.m])
            
            initial=[p.x,p.y,p.dx,p.dy]
            [timeL,YL]=integrate_ode(F,initial,self.time,self.time+timeChange)
            time=timeL[-1]
            Y=YL[-1]
            
            p.x=Y[0]
            p.y=Y[1]
            p.dx=Y[2]
            p.dy=Y[3]

            p.refreshPic()

        self.time=time
            

    
    















