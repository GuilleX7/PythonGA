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
        properties (dict<str, ?>): Dictionary containing all the properties
            required in order to apply the selection, like the amount of
            chromosomes to be selected or the selection pressure.
    """
    fitness_values = []
    for chromosome in chromosomes:
        fitness_value = fitness(chromosome)
        fitness_value = fitness_value if fitness_value >= 1 else 1
        fitness_values.append(fitness_value)
    
    return random.choices(chromosomes, fitness_values, k=properties["selection_amount"])

def tournament_selector_one_individual(chromosomes, fitness, properties):
    """
    Performs a tournament selection over a population of chromosomes.
    A given number k of chromosomes are randomly selected from the population,
    and only the best is selected for the next generation. 
    A chromosome can be selected multiple times.

    Args:
        chromosomes (list<list<number>>): Population of chromosomes
        fitness (function): Fitness function to be applied to the chromosomes
        properties (dict<str, ?>): Dictionary containing all the properties
            required in order to apply the selection, like the amount of
            chromosomes to be selected or the selection pressure.
    """
    chosen_chromosomes = random.sample(chromosomes,k=properties["selection_pressure"])
    select_chromosome= chosen_chromosomes[0]
    max_fitness=fitness(chosen_chromosomes[0])
    for i in range(len(chosen_chromosomes)-1):
        fitness_value = fitness(chosen_chromosomes[i+1])
        if max_fitness<fitness_value:
            max_fitness=fitness_value
            select_chromosome= chosen_chromosomes[i+1]
    return select_chromosome


def tournament_selector(chromosomes, fitness, properties):
    """
    The tournament selection procedure is repeated so the given amount 
    of chromosomes are passed to the next generation.

    Args:
        chromosomes (list<list<number>>): Population of chromosomes
        fitness (function): Fitness function to be applied to the chromosomes
        properties (dict<str, ?>): Dictionary containing all the properties
            required in order to apply the selection, like the amount of
            chromosomes to be selected or the selection pressure.
    """
    return [tournament_selector_one_individual(chromosomes, fitness, properties) for _ in range(properties["selection_amount"])]

        