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

    


#a function that controls what particles come next in the loop? so that way I can change it while the loop goes on?

#reformat ids
