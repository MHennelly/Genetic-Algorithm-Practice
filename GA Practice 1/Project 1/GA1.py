import random
import math

class Gene:
    def __init__(self, code):
        self.code = code
        self.cost = 9999

    def code(self):
        self.code = ''

    def rand(self, length):
        while(length > 0):
            self.code += str(chr(random.randrange(0,255,1)))
            length -= 1

    def calcCost(self, compareTo):
        total = 0
        for i in range(0,len(self.code)):
            total += (ord(self.code[i]) - ord(compareTo[i]) * ord(self.code[i]) - ord(compareTo[i]))
        self.cost = total

    def mate(self, gene):
        pivot = round(len(self.code)/2,0) - 1
        child1 = self.code[0:int(pivot)] + gene.code[int(pivot):]
        child2 = gene.code[0:int(pivot)] + self.code[int(pivot):]
        return [Gene(child1), Gene(child2)]

    def mutate(self, chance):
        if (random.uniform(0,1) > chance):
            return
        else:
            s = list(self.code)
            index = math.floor(random.uniform(0,1) * len(s))
            upOrDown = random.uniform(0,1)

            if (upOrDown > 0.5):
                s[index] = chr(ord(s[index]) + 1)
                self.code = ''
                self.code.join(s)
            else:
                s[index] = chr(ord(s[index]) - 1)
                self.code = ''
                self.code.join(s)

class Population:
    def __init__(self, goal, size):
        self.members = []
        self.goal = goal
        self.generationNumber = 0
        while (size > 0):
            gene = Gene('')
            gene.rand(len(self.goal))
            self.members.append(gene)
            size -= 1

    def generation(self):




        for i in range(0,10):
            for i in range(0,len(self.members)):
                self.members[i].calcCost(self.goal)

            for i in range(0, len(self.members)):
                print (self.members[i].code)

            for i in range(0,len(self.members) - 1,2):
                children = self.members[0].mate(self.members[1])


            for i in range(0,len(self.members)):
                self.members[i].mutate(0.5)
                self.members[i].calcCost(self.goal)
                if (self.members[i].code == self.goal):
                    print(self.members[i])
                    return True

            self.generationNumber += 1

population = Population("Hello, world!",20)
population.generation()
