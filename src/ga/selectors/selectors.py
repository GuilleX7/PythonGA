import random

def roulette_wheel_selector(chromosomes, fitness, properties):
    """
    Performs a roulette wheel selection over a population of chromosomes.
    Each chromosome has a probability of being selected proportional to
    its fitness value, which is calculated using the given fitness function.
    A chromosome can be selected multiple times.

    Non-positive fitness value will be assumed as 1 because chances can't be
    negative or 0.

    Args:
        chromosomes (list<list<number>>): Population of chromosomes
        fitness (function): Fitness function to be applied to the chromosomes
        properties (ProblemInstanceProperties): Class containing all the properties
            of the problem instance
    """
    if (properties.optimization_type == "MIN"):
        raise NotImplementedError("This selector cannot be used when optimization type is MIN")

    fitness_values = []
    for chromosome in chromosomes:
        fitness_value = fitness(chromosome)
        fitness_value = fitness_value if fitness_value >= 1 else 1
        fitness_values.append(fitness_value)

    return random.choices(chromosomes, fitness_values, k=properties.selection_amount)

def tournament_selector(chromosomes, fitness, properties):
    """
    Performs a tournament selection over a population of chromosomes.
    A given number k of chromosomes are randomly selected from the population,
    and only the best is selected for the next generation. 
    A chromosome can be selected multiple times.

    Args:
        chromosomes (list<list<number>>): Population of chromosomes
        fitness (function): Fitness function to be applied to the chromosomes
        properties (ProblemInstanceProperties): Class containing all the properties
            of the problem instance
    """
    cmp = max if properties.optimization_type == "MAX" else min
    return [cmp(random.sample(chromosomes, k=properties.selection_pressure), key=lambda x: fitness(x)) for _ in range(properties.selection_amount)]
