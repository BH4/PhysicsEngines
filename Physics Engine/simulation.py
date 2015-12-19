#Interpreter code

#things to change:
#simulation code should call move on the entire simulation. not just one particle. all movement decisions should come from kicks.py
#the spacecharge theta input is not used (add to the ntree class? then it might be stored on every node). it will be used in the spacecharge function in kicks.py
#spacecharge function has not been completed or tested




















#list of functions to be used by simulation code:
#simulation()
#sim.addParticle(**kwargs)
#sim.setTmax(tmax)
#sim.includeForce(force, [filename])
#sim.includeF


#sim.run()


#output types
#PosYvsTime

import sys
from vector import vector
from kicks import *
from particleList import particleList
from particle import particle
import matplotlib.pyplot as plt
from ntree import ntree

class simulation:

    def __init__(self):
        #inital setup
        self.particleList=particleList()
        self.forcesList=[]
        self.forceFiles=[]
        #self.spacecharge=ntree()
        self.tmax=None
        self.t=0.
        self.dt=.01

        #settings
        self.settingFunctions=[]#can create funtions later that will remove backwords particles or particles past a certain position

        #output
        self.outputFunctions=[]
        self.tracks=[]#this is not input. used internally
        self.timeData=[]#this is not input. used internally
        self.posData=[]#this is not input. used internally
        self.velData=[]#this is not input. used internally
        

    #setup    
    def setTmax(self,tmax):
        self.tmax=float(tmax)
        
    def addParticle(self,**kwargs):
        self.particleList.add(particle(**kwargs))

    def particleSet(self,numParticles):#creates set of identicle zero particles
        for i in xrange(numParticles):
            self.particleList(particle())
    
    #def uniformPos(self,disType,origin):#must be used after particleSet
        #disType
        #'circlexy'
        #'circlexz'
        #'circleyz'
        #'sphere'

    def includeForce(self,force,*args):
        if not(type(force) is str):
            print "force name must be string"
            sys.exit()

        self.forcesList.append(eval(force))
        
        if len(args)>1:
            print "input should be either (force) or (force,filename)"
            sys.exit()
        elif len(args)==1:
            filename=args[0]
            if not(type(filename) is str):
                print "filename must be string"
                sys.exit()
        else:
            filename=None

        self.forceFiles.append(filename)

    def includeOutput(self,*args):
        for o in args:
            self.outputFunctions.append(eval('self.'+o))

    def spacecharge3Dtree(self,theta):
        tree=ntree()
        tree=tree.fill(self.particleList)
        self.spacecharge=tree
        self.forceList('spacecharge')

    #durring the run
    def removeParticle(self,Id):#only used internally
        self.particleList.remove(Id)

    def addEvent(self,t,Id):#only used internally
        [Id,p]=self.particleList.get(Id)
        p.addEvent(t)
        '''
        Id=self.particleList.nextId(-1)
        while not(Id is None):
            p=self.particleList.get(Id)
            p.addEvent(t)
            Id=self.particleList.nextId(Id)
        '''
    def move(self,Id):#internal use only
        move(self.particleList,Id,self.t,self.dt,self.forcesList,self.forceFiles)
        
    #output
    def ripTracks(self):#internal use only
        Id=self.particleList.nextId(-1)
        while not(Id is None):
            [Id,p]=self.particleList.get(Id)
            self.tracks.append(p.getTrack())
            Id=self.particleList.nextId(Id)

        self.parseTracks()
        

    def parseTracks(self):#only used by ripTracks
        for track in self.tracks:
            t=[]
            pos=[]
            vel=[]
            for event in track:
                t.append(event[0])
                pos.append(event[1])
                vel.append(event[2])

            self.timeData.append(t)
            self.posData.append(pos)
            self.velData.append(vel)

    def getY(self):#only used after ripTracks
        yData=[]
        for posList in self.posData:
            y=[]
            for posSingle in posList:
                y.append(posSingle.getY())

            yData.append(y)

        return yData

    def getYV(self):#only used after ripTracks
        yvData=[]
        for velList in self.velData:
            yv=[]
            for velSingle in velList:
                yv.append(velSingle.getY())

            yvData.append(yv)

        return yvData

    def PosYvsTime(self,plotNum):#does this work for multiple p or does it overwrite the graphs?
        yData=self.getY()
        plt.figure(plotNum)
        for i in xrange(len(self.timeData)):
            plt.plot(self.timeData[i],yData[i])

        #plt.show()

    def VelYvsTime(self,plotNum):
        yvData=self.getYV()
        plt.figure(plotNum)
        for i in xrange(len(self.timeData)):
            plt.plot(self.timeData[i],yvData[i])

        #plt.show()
            

    def run(self):
        if not(self.tmax is None):
            self.dt=self.tmax/1000#this should be made beter
        else:
            self.dt=.01#this should be made beter
        done=False

        print 'Running'
        while not done:
            #check time
            if not(self.tmax is None):
                if self.t>=self.tmax:
                    done=True

            Id=self.particleList.nextId(-1)
            #check that there are still particles (they will be removed durring sim)
            if Id is None:
                done=True

            while not(Id is None):
                self.addEvent(self.t,Id)
                self.move(Id)
                
                Id=self.particleList.nextId(Id)

            self.t+=self.dt

        #maybe add the final events of all of the particles?
        print 'Finished Runnig'
        print 'Getting particle tracks'
        self.ripTracks()
        print 'creating output'
        plotNum=1;
        for f in self.outputFunctions:
            f(plotNum)
            plotNum+=1

        plt.show()
                    
            
        
