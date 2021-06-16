import random

def simple_mutator(chromosome, genes, probability):
    """
    Changes some genes with a given probability.

    Args:
        chromosome (list<number>): Chromosome to be mutated
        genes (list<number>): List of values that are allowed for a gene
        probability (number): Mutation probability
    """
    mutated_chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < probability:
            mutated_chromosome[i] = random.choice(genes)
    return mutated_chromosome
