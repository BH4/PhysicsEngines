import sys, random, pygame
from time import sleep
from particle import particle

def kill():
    pygame.quit()
    sys.exit()

#set up screen
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

a=pygame.draw.circle(screen, (0,255,0),(10,50),5,0)
print a.collidepoint

'''
#create the inital settings
n=20
particles=[]
for i in xrange(n):
    index=0
    while not(index==-1):
        radius=random.randint(10,20)
        x=random.randint(radius, width-radius)
        y=random.randint(radius, height-radius)
        p=particle((x,y), radius)
        prect=

        #test if there the particle collides with any others on the screen
        index=p.collidelist(particles)
    
    particles.append(p)
    p.display(screen)
'''
pygame.display.flip()

#loop
while 1:
    #sleep(.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kill()


