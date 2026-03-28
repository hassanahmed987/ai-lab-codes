import random
import string

# --- Configuration ---
TARGET = "HELLOWORLD"  # The "Goal" we want the AI to evolve toward
POP_SIZE = 100         # How many individuals in each generation
MUTATION_RATE = 0.01   # 1% chance a letter randomly changes

def get_fitness(guess):
    """Score: How many characters match the target exactly?"""
    score = 0
    for i in range(len(TARGET)):
        if guess[i] == TARGET[i]:
            score += 1
    return score

def create_individual():
    """Create a random string of the same length as the target."""
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(len(TARGET)))

# 1. Initialize Population
population = [create_individual() for _ in range(POP_SIZE)]

generation = 0
while True:
    # 2. Sort population by fitness (Best to Worst)
    population.sort(key=lambda x: get_fitness(x), reverse=True)
    
    best_guess = population[0]
    print(f"Gen {generation}: {best_guess} (Fitness: {get_fitness(best_guess)})")

    # If we found the target, we are done!
    if best_guess == TARGET:
        break

    # 3. Selection (Keep the top 10% as parents)
    new_generation = population[:10]

    # 4. Breeding (Fill the rest of the population with children)
    while len(new_generation) < POP_SIZE:
        parent1 = random.choice(population[:50]) # Pick from top 50
        parent2 = random.choice(population[:50])
        
        # Crossover: Split parents in the middle and swap
        split = len(TARGET) // 2
        child = parent1[:split] + parent2[split:]
        
        # 5. Mutation: Randomly change a letter
        child_list = list(child)
        for i in range(len(child_list)):
            if random.random() < MUTATION_RATE:
                child_list[i] = random.choice(string.ascii_uppercase)
        
        new_generation.append("".join(child_list))

    population = new_generation
    generation += 1
