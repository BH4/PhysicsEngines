#need to make 'origin' an input to the functions. That way const functions can be applied at different positions








#apply kicks to particles, also contains the differential equations for the kicks?
from vector import vector
from particle import particle
from RungeKutta import RK4
#from simulation import simulation

def move(particleList,Id,t,dt,a,files):
    # 'a' is a list of functions to be called to evaluate the total acceleration at any point
    [pos,vel,t]=RK4(particleList,Id,t,dt,a,files)

    #update the particle
    [Id,particle]=particleList.get(Id)
    particle.setPos(pos)
    particle.setVel(vel)


#internal use functions for simplified calculations in elements defined later
#these return a force
def EField(q,E):#(q (int), E (vector))
    return E*q

def BField(q,vel,B):#(q (int), vel (vector), B (vector))
    return (vel.cross(B))*q

def GField(m,G):#(m (int), G(vector))
    return G*m






# each function should return the vector acceleration of particle 'id' given particleList,id,t,filename
# pos,vel,particleList,Id,t,filename are passed to each function
#pos,vel: because these change multiple times in RK4 they cant be set within the particle and must be passed separatly. (it is easier this way)
#particleList: the particleList that the particle being kicked is part of
#Id: Id in particle list of the particle being kicked
#t: simulation time
#filename: name of a file that may be used in calculation of acceleration
#          possibly to specify a field (not used yet

def EarthG(pos,vel,particleList,Id,t,filename):
    return vector(x=0,y=-9.8,z=0)

def constEfeild(pos,vel,particleList,Id,t,filename):
    [Id,particle]=particleList.get(Id)
    charge=particle.q*particle.nq
    mass=particle.mass
    
    return vector(x=0,y=charge*2/mass,z=0)



#def spacecharge(particleList,Id,t,filename):
