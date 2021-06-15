class Problem:
    """
    This class represents a genetic algorithm using value-in-range chromosomes,
    allowing to solve some genetic problems like the Knapsack problem.
    """
    def __init__(self, genes, individuals_length, decode, fitness):
        """
        Constructor for the genetic problem.

        Args:
            genes (list<number>): List of values that are allowed for a gene
            individuals_length (number): Number of genes a chromosome has
            decode (function): Function that takes a chromosome and generates a
                solution for the problem
            fitness (function): Function that takes a solution to the problem and
                calculates the value to be optimized
        """
        self.genes = genes
        self.individuals_length = individuals_length
        self.decode = decode
        self.fitness = fitness