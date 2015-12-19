from math import cos, sin, pi
from vector import vector
#x positive == right
#y positive == down
#phi=0 == right
#phi=pi/2 == down
#theta=0==+z==into the page


#in the future maybe store only events, instead of particle positions and velocitys. that way time would be stored as well




#sys.exit()
class particle:
    G=6.67384e-11
    e_0=8.854187817e-12
    c=299792458
    q=1.60217657e-19
    #me=
    #mp=

    #can take input of x,y,z,speed,phi,theta,mass,nq
    #all have default values. all defaults are zero
    #can also input speed by its x,y,z components as xv, yv, zv
    def __init__(self, **kwargs):#x,y,z), speed, phi, theta, size, mass, e, (r,g,b)):
        keys=kwargs.keys()
        
        #position input
        if keys.count('x')==0:
            x=0
        else:
            x=kwargs['x']
        if keys.count('y')==0:
            y=0
        else:
            y=kwargs['y']
        if keys.count('z')==0:
            z=0
        else:
            z=kwargs['z']
        self.pos=vector(x=x,y=y,z=z)

        #velocity input
        if keys.count('speed')==0 and keys.count('phi')==0 and keys.count('theta')==0:
            #velocity input as cartesian
            if keys.count('xv')==0:
                xv=0
            else:
                xv=kwargs['xv']
            if keys.count('yv')==0:
                yv=0
            else:
                yv=kwargs['yv']
            if keys.count('zv')==0:
                zv=0
            else:
                zv=kwargs['zv']
            self.vel=vector(x=xv, y=yv, z=zv)

        else:
            #velocity input as spherical
            if keys.count('speed')==0:
                speed=0
            else:
                speed=kwargs['speed']
            if keys.count('phi')==0:
                phi=0
            else:
                phi=kwargs['phi']
            if keys.count('theta')==0:
                theta=0
            else:
                theta=kwargs['theta']
            self.vel=vector(r=speed, phi=phi, theta=theta)

        #other input
        if keys.count('mass')==0:
            mass=0
        else:
            mass=kwargs['mass']
        self.mass=float(mass)
        
        if keys.count('density')==0:
            density=0
        else:
            density=kwargs['density']
        self.density=density
        
        if keys.count('nq')==0:
            nq=0
        else:
            nq=kwargs['nq']
        self.nq=nq

        #non-input. used by simulation object
        self.track=[]#holds sets of (t,pos,vel) one 'event'        
        
    
    def __eq__(self, other):
        return self.__dict__==other.__dict__

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel

    def getQ(self):
        return q*nq

    def setPos(self,pos):
        self.pos=pos

    def setVel(self,vel):
        self.vel=vel

    def addEvent(self,t):
        self.track.append((t,self.pos,self.vel))

    def getTrack(self):
        return self.track
