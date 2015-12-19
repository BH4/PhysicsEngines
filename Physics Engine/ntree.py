#make more specific instead of general. could just do the entire barns-hut algorithm
from vector import vector
from copy import deepcopy
from particleList import particleList

class ntree:

    def __init__(self,m):
        [minx,maxx,miny,maxy,minz,maxz]=m
        nodes=[]#array of ntrees
        self.minx=float(minx)
        self.maxx=float(maxx)
        self.miny=float(miny)
        self.maxy=float(maxy)
        self.minz=float(minz)
        self.maxz=float(maxz)

        center=None
        charge=None

    def add(self,tree):
        self.nodes.append(tree)

    def addParticle(self,p):
        self.particle=p

    def fill(self,particleList):
        L=deepcopy(particleList)

        if L.num()==0:
            return self
        elif L.num()==1:
            p=L.get(nextId(-1))
            self.center=p.getPos()
            self.charge=float(p.getQ)
            return self

        #listed in order of minx,maxx,miny,maxy,minz,maxz
        midx=(self.minx+self.maxx)/2
        midy=(self.miny+self.maxy)/2
        midz=(self.minz+self.maxz)/2
        boundaries=[[midx,self.maxx,midy,self.maxy,midz,self.maxz],
                    [midx,self.maxx,midy,self.maxy,self.minz,midz],
                    [self.minx,midx,midy,self.maxy,self.minz,midz],
                    [self.minx,midx,midy,self.maxy,midz,self.maxz],
                    [midx,self.maxx,self.miny,midy,midz,self.maxz],
                    [midx,self.maxx,self.miny,midy,self.minz,midz],
                    [self.minx,midx,self.miny,midy,self.minz,midz],
                    [self.minx,midx,self.miny,midy,midz,self.maxz]]
        
        for i in xrange(8):
            [cropped,L]=L.crop(boundaries(i))
            t=ntree(boundaries(i))
            self.add(t.fill(cropped))

        chargeTot=0
        centerTimesChargeSum=vector(x=0,y=0,z=0)
        for i in xrange(8):
            if not(self.nodes(i).charge is None):
                chargeTot+=self.nodes(i).charge
                centerTimesChargeSum=centerTimesChargeSum+(self.nodes(i).center)*(self.nodes(i).charge)

        self.charge=chargeTot
        self.center=centerTimesChargeSum*(1/chargeTot)

        return self


    #def BH(self,particleList,particle,theta):
        





                
