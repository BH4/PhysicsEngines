from math import acos, atan, sqrt, sin, cos,  pi


class vector:
    def __init__(self, x, y, z):#phi is x-y plane, theta=0==+z axis
        x=float(x)
        y=float(y)
        z=float(z)
        self.x=x
        self.y=y
        self.z=z

        r2=x**2+y**2+z**2
        r=sqrt(r2)
        if r==0:
            theta=0
        else:
            theta=acos(z/r)
        if x==0:
            phi=pi/2
        else:
            phi=atan(y/x)
        if x<0:
            phi=pi+phi

        self.r2=r2
        self.r=r
        self.theta=theta%(2*pi)
        self.phi=phi%(2*pi)

    def __eq__(self, other):
        return self.__dict__==other.__dict__

    @staticmethod
    def convert(r, phi, theta):
        r=float(r)
        phi=float(phi)
        theta=float(theta)
        st=sin(theta)
        sp=sin(phi)
        cp=cos(phi)
        ct=cos(theta)

        x=r*st*cp
        y=r*st*sp
        z=r*ct

        return vector(x,y,z)

    #gets
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getR(self):
        return self.r

    def getR2(self):
        return self.r2

    def getTheta(self):
        return self.theta

    def getPhi(self):
        return self.phi



    

    def vectorSum(self, other):
        x=self.x+other.x
        y=self.y+other.y
        z=self.z+other.z

        return vector(x,y,z)

    def vectorMinus(self, other):
        x=self.x-other.x
        y=self.y-other.y
        z=self.z-other.z

        return vector(x,y,z)

    def unitVector(self):
        return vector.convert(1.,self.phi,self.theta)

    def dotProduct(self, other):
        x=self.x*other.x
        y=self.y*other.y
        z=self.z*other.z

        return x+y+z

    def byScalar(self,n):
        return vector(self.x*n,self.y*n,self.z*n)
