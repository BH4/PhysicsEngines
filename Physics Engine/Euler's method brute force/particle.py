import pygame
from math import cos, sin, pi
from vector import vector
#x positive == right
#y positive == down
#phi=0 == right
#phi=pi/2 == down
#theta=0==+z==into the page




class particle:
    G=6.67384e-11

    
    def __init__(self, (x,y,z), speed, phi, theta, size, mass, e, (r,g,b)):
        self.pos=vector(x,y,z)
        self.vel=vector.convert(speed, phi, theta)
        self.size=float(size)
        self.mass=float(mass)
        #self.density=density

        self.restitution=float(e)
        
        self.color=(r,g,b)
        self.thickness=0

    def __eq__(self, other):
        return self.__dict__==other.__dict__

    def getPos(self):
        return self.pos

    def display(self, window):#, depth):#depth is only important for the color
        #c=self.getColor(depth)#the color part only works well if bounce is on
        pygame.draw.circle(window, self.color, (int(self.pos.getX()), int(self.pos.getY())), int(self.size), self.thickness)

#    def getColor(self, depth): # oould compleate this by having red start at zero then slowly become green then blue as particle gets further back, total of the colors is always 255
#        z=self.z
#        if z>

    def undisplay(self, window, bgcolor):
        pygame.draw.circle(window, bgcolor, (int(self.pos.getX()), int(self.pos.getY())), int(self.size), self.thickness)
    
    def move(self):
        self.pos=self.pos.vectorSum(self.vel)

    def bounce(self, width, height):#only used for 2D bouncing off of boarders
        newX=self.pos.getX()
        newY=self.pos.getY()
        newPhi=self.vel.getPhi()
        change=False
        
        if self.pos.getX() > width -self.size:
            newX=2*(width - self.size) - self.pos.getX()
            newPhi=pi-newPhi
            change=True
            
        elif self.pos.getX()<self.size:
            newX=2*self.size -self.pos.getX()
            newPhi=pi-newPhi
            change=True

        if self.pos.getY() > height - self.size:
            newY=2*(height - self.size) - self.pos.getY()
            newPhi=-newPhi
            change=True

        elif self.pos.getY() < self.size:
            newY=2*self.size - self.pos.getY()
            newPhi=-newPhi
            change=True

        if change:
            self.pos=vector(newX,newY,0)
            self.vel=vector.convert(self.vel.getR(),newPhi,self.vel.getTheta())

    def bounce3D(self, width, height, depth):#only used for 3D bouncing off of boarders
        newX=self.pos.getX()
        newY=self.pos.getY()
        newZ=self.pos.getZ()
        newPhi=self.vel.getPhi()
        newTheta=self.vel.getTheta()
        change=False
        
        if self.pos.getX() > width -self.size:
            newX=2*(width - self.size) - self.pos.getX()
            newPhi=pi-newPhi
            change=True
            
        elif self.pos.getX()<self.size:
            newX=2*self.size -self.pos.getX()
            newPhi=pi-newPhi
            change=True

        if self.pos.getY() > height - self.size:
            newY=2*(height - self.size) - self.pos.getY()
            newPhi=-newPhi
            change=True

        elif self.pos.getY() < self.size:
            newY=2*self.size - self.pos.getY()
            newPhi=-newPhi
            change=True

        if self.pos.getZ() < self.size:
            newZ=2*self.size - self.pos.getZ()
            newTheta=pi-newTheta
            change=True

        elif self.pos.getZ() > depth-self.size:
            newZ=2*(depth-self.size) - self.pos.getZ()
            newTheta=pi-newTheta
            change=True

        if change:
            self.pos=vector(newX,newY,newZ)
            self.vel=vector.convert(self.vel.getR()*self.restitution,newPhi,newTheta)

    def collide(self, other):
        rvector=other.pos.vectorMinus(self.pos)#vector pointing from self to other
        
        if rvector.getR2()<(self.size+other.size)**2:
            penetrationDepth=(self.size+other.size)-rvector.getR()
            normal=rvector.unitVector()
            rv=other.vel.vectorMinus(self.vel)

            velAlongNormal=rv.dotProduct(normal)
            #print velAlongNormal

            if velAlongNormal<-.1:
                e=min(self.restitution, other.restitution)

                j=-(1+e)*velAlongNormal
                j/=1/self.mass + 1/other.mass

                impulseSelf=normal.byScalar(j/self.mass)#vector.convert(j/self.mass,normal.getPhi(),normal.getTheta())
                impulseOther=normal.byScalar(j/other.mass)#vector.convert(j/other.mass,normal.getPhi(),normal.getTheta())
                
                self.vel=self.vel.vectorMinus(impulseSelf)
                other.vel=other.vel.vectorSum(impulseOther)

                self.positionalCorrection(other,penetrationDepth,normal)
                

            elif velAlongNormal<=0:
                return self.combine(other)

        return None

    def positionalCorrection(self, other, penetrationDepth, normal):
        percent = .5 # usually 20% to 80%
        slop = 0.02 # usually 0.01 to 0.1

        correctionMag=max(penetrationDepth-slop, 0)/(self.mass+other.mass)*percent
        correctionSelf=normal.byScalar(correctionMag/self.mass)
        correctionOther=normal.byScalar(correctionMag/other.mass)

        self.pos=self.pos.vectorMinus(correctionSelf)
        other.pos=other.pos.vectorSum(correctionOther)

    def combine(self, other):
        mass=self.mass+other.mass
        comPos=((self.pos.byScalar(self.mass)).vectorSum(other.pos.byScalar(other.mass))).byScalar(1/mass)
        finalVel=((self.vel.byScalar(self.mass)).vectorSum(other.vel.byScalar(other.mass))).byScalar(1/mass)
        newColor=((self.color[0]+other.color[0])/2,(self.color[1]+other.color[1])/2,(self.color[2]+other.color[2])/2)

        new=particle((0,0,0),0,0,0,1,1,1,(0,0,0))
        new.pos=comPos
        new.vel=finalVel
        new.size=(self.size**3+other.size**3)**(1./3)
        new.mass=mass
        new.restitution=(self.restitution+other.restitution)/2
        new.color=newColor#can add proportions by volume to the colors (e.g. selfcolor*1/3+other*2/3)

        return new
        
        

    def gravity(self, other):
        if not(self.mass==0):
            rvector=other.pos.vectorMinus(self.pos)
                
            if rvector.getR()>0 and rvector.getR2()>(self.size+other.size)**2: 
                mag=(particle.G*other.mass)/rvector.getR2()
                AfromO=vector.convert(mag,rvector.getPhi(),rvector.getTheta())
                self.vel=self.vel.vectorSum(AfromO)
                


