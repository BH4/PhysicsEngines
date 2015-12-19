from particle import particle

class particleList:
    currId=0
    
    def __init__(self):
        self.list=[]
        self.ids=[]

    def add(self,particle):
        global currId
        self.list.append(particle)
        self.ids.append(particleList.currId)
        particleList.currId+=1

    def num(self):
        return len(self.ids)

    def remove(self,Id):
        #print self.ids
        i=self.ids.index(Id)
        self.list.pop(i)
        self.ids.pop(i)

    def get(self, Id):
        c=self.ids.count(Id)
        if c>0:
            index=self.ids.index(Id)
            return [self.ids[index],self.list[index]]

        return [None,None]

    def nextId(self, Id):
        if Id>=particleList.currId:
            return None

        c=0
        while c==0:
            Id+=1
            
            if Id>=particleList.currId:
                return None
            
            c=self.ids.count(Id)

        return Id

    def crop(self,m):
        [minx,maxx,miny,maxy,minz,maxz]=m
        new=particleList()
        others=particleList()
        Id=self.nextId(-1)
        while not(Id is None):
            p=get(Id)
            pos=p.getPos()
            x=pos.getX()
            y=pos.getY()
            z=pos.getZ()

            if x>=minx and x<=maxx and y>=miny and y<=maxy and z>=minz and z<=maxz:
                new.add(p)
            else:
                others.add(p)

        return [new,others]
    '''
    def sort(self):#changes all the id values 
        z=[]
        for p in self.list:
            z.append(p.getPos().getZ())

        sortThis=zip(z,self.list)
        sort=sorted(sortThis)
        apart=zip(*sort)

        self.list=list(apart[1])
        self.list.reverse()
        self.ids=range(len(self.list))

    '''



