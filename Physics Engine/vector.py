from math import acos, atan, sqrt, sin, cos,  pi


class vector:

    #must name the input
    def __init__(self, **kwargs):#phi is x-y plane, theta=0==+z axis
        #assumes input is either xyz or r phi theta.
        keys=kwargs.keys()
        if keys==['x','y','z'] or keys==['x','z','y'] or keys==['y','x','z'] or keys==['y','z','x'] or keys==['z','x','y'] or keys==['z','y','x']:
            x=float(kwargs['x'])
            y=float(kwargs['y'])
            z=float(kwargs['z'])
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
        elif not(keys==[]):
            r=float(kwargs['r'])
            phi=float(kwargs['phi'])
            theta=float(kwargs['theta'])
            self.r=r
            self.r2=r*r
            self.phi=phi
            self.theta=theta
            
            st=sin(theta)
            sp=sin(phi)
            cp=cos(phi)
            ct=cos(theta)

            self.x=r*st*cp
            self.y=r*st*sp
            self.z=r*ct
        else:
            self.x=0.
            self.y=0.
            self.z=0.
            self.r=0.
            self.r2=0.
            self.phi=0.
            self.theta=0.

    def __eq__(self, other):
        return self.__dict__==other.__dict__

    def __add__(self, other):
        return vector(x=self.x+other.x,y=self.y+other.y,z=self.z+other.z)

    #instance*int. must be in the correct order
    def __mul__(self, const):
        return vector(x=self.x*const,y=self.y*const,z=self.z*const)

    ''' this code shouldn't be nescessary with the use of **kwargs
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
    '''
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
        return vector(r=1.,phi=self.phi,theta=self.theta)

    def dotProduct(self, other):
        x=self.x*other.x
        y=self.y*other.y
        z=self.z*other.z

        return x+y+z

    def byScalar(self,n):
        return vector(self.x*n,self.y*n,self.z*n)

    def cross(other):
        x=self.y*other.z-other.y*self.z
        y=other.x*self.z-self.x*other.z
        z=self.x*other.y-other.x*self.y
        
        return vector(x,y,z)
