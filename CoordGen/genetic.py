import random
import sys

x_goal = int(input("Please enter an x value: "))
y_goal = int(input("Please enter a y value: "))

class Chromosome:
    def __init__(self):
        self.x_value = 0
        self.y_value = 0
        self.cost = 0

    def rand(self):
        self.x_value = random.randrange(0,100,1)
        self.y_value = random.randrange(0,100,1)

    def calculateCost(self):
        x_difference = abs(self.x_value - x_goal)
        y_difference = abs(self.y_value - y_goal)
        self.cost = x_difference + y_difference

    def mate_x(self, parent):
        child = Chromosome()
        child.x_value = parent.x_value
        child.y_value = self.y_value
        return child

    def mate_y(self, parent):
        child = Chromosome()
        child.x_value = self.x_value
        child.y_value = parent.y_value
        return child

    def mutate(self):
        chance = random.uniform(0,1)
        if (chance > 0.99):
            return
        else:
            x_or_y = random.uniform(0,1)
            up_or_down = random.uniform(0,1)
            if (x_or_y > 0.5):
                if (up_or_down > 0.5):
                    self.x_value += 0.5
                else:
                    self.x_value -= 0.5
            else:
                if (up_or_down > 0.5):
                    self.y_value += 0.5
                else:
                    self.y_value -= 0.5

class Population:
    def __init__(self):
        self.members = []
        self.generationNumber = 0
        size = 100
        while (size > 0):
            point = Chromosome()
            point.rand()
            self.members.append(point)
            size -= 1

    def generation(self):
        while(self.generationNumber < 1000):
            self.generationNumber += 1
            print('Generation: ' + str(self.generationNumber))

            for i in range(0,len(self.members)):
                self.members[i].calculateCost()

            for i in range(0,2):
                print(str(self.members[i].x_value))
                print(str(self.members[i].y_value))
                print('Cost: ' + str(self.members[i].cost))

            self.members.sort(key=lambda point: point.cost)

            child1 = self.members[0].mate_x(self.members[1])
            child2 = self.members[1].mate_y(self.members[0])

            for i in range(0, len(self.members), 2):
                self.members[i] = child1

            for i in range(1, len(self.members), 2):
                self.members[i] = child2

            for i in range(len(self.members)):
                self.members[i].mutate()
                self.members[i].calculateCost()
                if (self.members[i].cost == 0):
                    print('Goal achieved')
                    print(str(self.members[i].x_value))
                    print(str(self.members[i].y_value))
                    sys.exit()

population = Population()
population.generation()