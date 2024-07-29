import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 5  # Slower for better observation of equilibrium

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Organism properties
LIFESPAN = 50
REPRODUCTION_AGE = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life Simulation")
clock = pygame.time.Clock()

class Organism:
    def __init__(self, x, y, strength):
        self.x = x
        self.y = y
        self.strength = strength
        self.age = 0
        self.interaction_count = 0  # Count interactions for elimination logic
    
    def move(self):
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
        self.x = (self.x + dx) % GRID_WIDTH
        self.y = (self.y + dy) % GRID_HEIGHT
    
    def age_and_maybe_die(self):
        self.age += 1
        return self.age > LIFESPAN
    
    def reproduce(self):
        return self.age > REPRODUCTION_AGE and random.random() < 0.5  # 50% chance to reproduce
    
    def interact(self, other):
        if self.interaction_count == 1:  # Second interaction
            if self.strength > other.strength:
                return True  # This organism eliminates the other
        self.interaction_count += 1
        return False  # No elimination

def create_initial_population():
    return [Organism(random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1), random.randint(1, 10)) for _ in range(50)]

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

def draw_population(population):
    for organism in population:
        pygame.draw.rect(screen, GREEN, (organism.x * CELL_SIZE, organism.y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    population = create_initial_population()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid()
        draw_population(population)

        new_population = []
        for organism in population:
            organism.move()
            if organism.age_and_maybe_die():
                continue
            if organism.reproduce():
                new_population.append(Organism(organism.x, organism.y, random.randint(1, 10)))
            new_population.append(organism)

        # Resolve interactions
        positions = {}
        for organism in new_population:
            pos = (organism.x, organism.y)
            if pos in positions:
                other = positions[pos]
                if organism.interact(other):
                    continue  # Current organism eliminates the other
                if other.interact(organism):
                    continue  # Other organism eliminates the current
            positions[pos] = organism
        
        population = list(positions.values())
        
        # Regenerate organisms if population is low
        if len(population) < 50:
            for _ in range(5):
                x, y = random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)
                population.append(Organism(x, y, random.randint(1, 10)))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()