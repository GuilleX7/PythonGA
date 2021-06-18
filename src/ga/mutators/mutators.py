import random

def simple_mutator(chromosome, genes, properties):
    """
    Changes some genes with a given probability.

    Args:
        chromosome (list<number>): Chromosome to be mutated
        genes (list<number>): List of values that are allowed for a gene
        properties (ProblemInstanceProperties): Class containing all the properties
            of the problem instance
    """
    mutated_chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if random.random() < properties.mutation_probability:
            mutated_chromosome[i] = random.choice(genes)
    return mutated_chromosome
