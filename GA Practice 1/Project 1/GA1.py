import random
import sys

class Gene:
    def __init__(self, code, goal):
        self.code = code
        self.cost = 9999
        self.goal = goal

    def code(self):
        self.code = ''

    def rand(self, length):
        while(length > 0):
            self.code += str(chr(random.randrange(33,123,1)))
            length -= 1

    def calcCost(self, compareTo):
        total = 0
        for i in range(0,len(self.code)):
            total += ((ord(self.code[i]) - ord(compareTo[i])) * (ord(self.code[i]) - ord(compareTo[i])))
        self.cost = total

    def mate_one(self, gene):
        pivot = round(len(self.code)/2,0) - 1
        child1 = self.code[0:int(pivot)] + gene.code[int(pivot):]
        return Gene(child1, self.goal)

    def mate_two(self, gene):
        pivot = round(len(self.code)/2,0) - 1
        child2 = gene.code[0:int(pivot)] + self.code[int(pivot):]
        return Gene(child2, self.goal)

    def mutate(self, chance):
        if chance > random.uniform(0,1):
            return
        else:
            s = list(self.code)
            mutation = ''
            index = random.randint(0,len(self.code) - 1)
            upOrDown = random.uniform(0,1)
            if upOrDown > 0.5:
                s[index] = chr(ord(s[index]) + 1)
            else:
                s[index] = chr(ord(s[index]) - 1)
            for i in range (0,len(s)):
                mutation += str(s[i])
            self.code = mutation

def sort_pop(self, member):
    return member.cost

class Population:
    def __init__(self, goal, size, generations):
        self.members = []
        self.goal = goal
        self.generationNumber = 0
        self.generations = generations
        while (size > 0):
            gene = Gene('', goal)
            gene.rand(len(self.goal))
            self.members.append(gene)
            size -= 1



    def generation(self):
        while(self.generationNumber < self.generations):
            self.generationNumber += 1
            print('Generation: ' + str(self.generationNumber))

            for i in range(0,len(self.members)):
                self.members[i].calcCost(self.goal)

            self.members.sort(key =lambda gene: gene.cost)

            for i in range(0,2):
                print (self.members[i].code)
                print ('Cost: ' + str(self.members[i].cost))

            child1 = self.members[0].mate_one(self.members[1])
            child2 = self.members[0].mate_two(self.members[1])

            for i in range(0,len(self.members),2):
                self.members[i] = child1

            for i in range(1,len(self.members),2):
                self.members[i] = child2

            for i in range(0, len(self.members)):
                self.members[i].mutate(.99)
                self.members[i].calcCost(self.goal)
                if (self.members[i].code == self.goal):
                    print('Generation: ' + str(self.generationNumber))
                    print(self.members[i].code)
                    print('Cost: ' + str(self.members[i].cost))
                    print('Goal: ' + "'" + str(self.members[i].code) + "'" + ' achieved')
                    sys.exit()

print('Welcome!')
goal = input('Please enter a phrase:')
population = Population(goal,100,10000)
population.generation()
