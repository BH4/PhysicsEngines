import sys, random, pygame
from time import sleep
from particle import particle
from math import pi
from particleList import particleList

def kill():
    pygame.quit()
    sys.exit()

def randomParticles(n, width, height, depth):#create the inital settings
    particles=particleList()
    for i in xrange(n):
        radius=4#random.randint(10,20)
        x=random.randint(radius, width-radius)
        y=random.randint(radius, height-radius)
        z=random.randint(radius, depth-radius)
        speed=0#random.random()
        phi=random.uniform(0,2*pi)
        theta=random.uniform(0,pi)
        mass=random.random()*1e11+1e10
        e=random.uniform(0,1)
        color=(random.random()*200+55,random.random()*200+55,random.random()*200+55)
        particles.add(particle((x,y,z), speed, phi, theta, radius, mass, e, color))

    return particles


#set up screen
width = 800
height = 600
depth =700 #only necessary if a boundary is enforced
screen = pygame.display.set_mode((width, height))
bgcolor = (0, 0, 0)

particles=particleList()

particles=randomParticles(20, width, height, depth)                                                         #random function
#particles.add(particle((400,300,400),.8,pi/2,pi,10,1e11,1,(0,0,255)));particles.add(particle((408,300,500),.8,pi/2,0,10,1e11,1,(0,0,255)))          #two particles going opposite directions until they bounce off z walls
#particles.add(particle((350,300,350),.2,pi/2,pi/2,4,1e11,1,(0,0,255)));particles.add(particle((450,300,350),.2,-pi/2,pi/2,4,1e11,1,(0,0,255)))  #two particles orbiting x-y plane
#particles.add(particle((300,300,350),0,0,pi/2,8,5e10,.8,(0,0,255)));particles.add(particle((500,300,350),0,pi,pi/2,8,1e11,.8,(0,0,255)))           #two particles hitting each other head on
#particles.add(particle((300,300,350),.1,pi/2,pi/2,10,-1e10,.2,(0,0,255)));particles.add(particle((500,300,350),.1,pi/2,pi/2,10,1e10,.2,(0,0,255))) #negative mass. ends with division by zero
#particles.add(particle((400,300,350),0,pi/2,pi/2,30,1e15,.2,(0,0,255)));particles.add(particle((600,300,350),20,pi/2,pi/2,8,1e10,1,(0,0,255)))   #small body orbiting large. turn on sleep. ends in int overflow?
#particles.add(particle((350,300,350),.2,pi/2,0,4,1e11,1,(255,0,0)));particles.add(particle((450,300,350),.2,-pi/2,pi,4,1e11,1,(0,0,255)))  #two particles orbiting x-z plane
#particles.add(particle((400,300,350),0,pi/2,pi/2,30,1e15,.2,(0,0,255)));particles.add(particle((600,300,350),20,pi/2,pi,8,1e10,1,(0,0,0)))    #invisible object orbits large object

#loop
while 1:
    sleep(.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kill()

    particles.sort()
    #undisplay loop: only necessary so that we dont see a black spot in the previous position (normally not noticable unless it is currently infront of a large color object
    Id=particles.nextId(-1)
    while not(Id is None):
        [Id,p]=particles.get(Id)#returns particle and its id
        p.undisplay(screen, bgcolor)
        Id=particles.nextId(Id)

    Id=particles.nextId(-1)
    while not(Id is None):
        removed=False
        [Id,p]=particles.get(Id)#returns particle and its id
        
        
        p.move()
        p.bounce3D(width, height, depth)

        #forces
        Id2=particles.nextId(-1)
        while not(Id2 is None):
            [Id2,p2]=particles.get(Id2)
            if not(p==p2):
                p.gravity(p2)

            Id2=particles.nextId(Id2)

        #collisions
        Id2=particles.nextId(Id)

        while not(Id2 is None) and not(removed):
            [Id2,p2]=particles.get(Id2)

            new=p.collide(p2)
            if not(new is None):
                removed=True
                particles.add(new)
                
                p.undisplay(screen,bgcolor)
                particles.remove(Id)
                p2.undisplay(screen,bgcolor)
                particles.remove(Id2)

            Id2=particles.nextId(Id2)

        Id=particles.nextId(Id)
        
        if not removed:
            p.display(screen)

    pygame.display.flip()

    


