

import random
import numpy as np

## lets consider planet a grid and assume this a grid of 10X10
PLANET_SIZE = 10 ### assume the size of the planet grid mean(10X10)

INITIAL_POPULATION = 10 ### let the initial population of living organisms

MAX_LIFESPAN = 30 ### let the maximum lifespan of a living organism

STRENGTH_RANGE = (1, 10) ## lets consider strength between 1 to 10

RESOURCE_REGENERATION_RATE = 0.1  ## lets assume resources are regenerated woth some rate

class Organism:
    def __init__(self):
        self.strength = random.randint(*STRENGTH_RANGE)
        self.lifespan = MAX_LIFESPAN
        self.position = (random.randint(0, PLANET_SIZE-1), random.randint(0, PLANET_SIZE-1))

    def move(self):
        x = random.randint(-1, 1)
        y = random.randint(-1, 1)
        #print(x,y)
        #print(self.position[0])
        new_x = (self.position[0] + x) % PLANET_SIZE
        new_y = (self.position[1] + y) % PLANET_SIZE
        #print(new_x,new_y)
        self.position = (new_x, new_y)

    def interact(self, other):
        if isinstance(other,Organism) and self.strength > other.strength:
            other.lifespan = 0
        elif isinstance(other,Organism) and self.strength < other.strength:
            self.lifespan = 0

    def reproduce(self):
        if self.lifespan > 0 and random.random() < 0.1:
            offspring = Organism()
            offspring.position = self.position
            return offspring
        return None
    
    def update(self):
        self.lifespan -= 1


class Planet:
    def __init__(self):
        self.grid = np.zeros((PLANET_SIZE, PLANET_SIZE), dtype=object)
        self.resources = np.ones((PLANET_SIZE, PLANET_SIZE))

    def add_organism(self, organism):
        self.grid[organism.position] = organism
        print('organism added at',organism.position)


    def remove_organism(self, organism):
        print('organism removed from',organism.position)
        self.grid[organism.position] = None


    def update_resources(self):
        self.resources += RESOURCE_REGENERATION_RATE
        self.resources[self.resources > 1] = 1


    def simulate_step(self):
        new_organisms = []
        for i in range(PLANET_SIZE):
            for j in range(PLANET_SIZE):
                organism = self.grid[i, j]
                if isinstance(organism, Organism):
                    organism.move()
                    other_organism = self.grid[organism.position]
                    organism.interact(other_organism)
                    offspring = organism.reproduce()
                    if offspring is not None:
                        new_organisms.append(offspring)
                    organism.update()
                    if organism.lifespan <= 0:
                        self.remove_organism(organism)
        for organism in new_organisms:
            self.add_organism(organism)
        self.update_resources()


planet = Planet()
for _ in range(INITIAL_POPULATION):
    organism = Organism()
    planet.add_organism(organism)


while True:
    planet.simulate_step()
    if len(planet.grid[planet.grid != None]) == INITIAL_POPULATION:
        ##print(len(planet.grid[planet.grid != None]))
        break

print("Simulation reached equilibrium!")
