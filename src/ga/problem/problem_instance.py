import random
from problem.problem_instance_properties import ProblemInstanceProperties
from mutators.mutators import simple_mutator
from crossovers.crossovers import single_point_crossover
from selectors.selectors import tournament_selector


class ProblemInstance:
    """
    Class that represents an instantiated genetic problem, containing
    everything related with the populations and the mutation and crossover
    mechanisms.
    """

    def __init__(self, problem, mutator=simple_mutator, crossover=single_point_crossover, selector=tournament_selector, properties=ProblemInstanceProperties(), initial_population=None):
        """
        Constructor for the class.

        Args:
            problem (Problem): Genetic problem
            mutator (function): Mutator function used for the chromosome mutations
            crossover (function): Crossover function used for performing crossover over two individuals
            selector (function): Selection function used in order to select the individuals for the next
                generation
            properties (ProblemInstanceProperties): Class containing all the properties
                of the problem instance
            initial_population (list<number>): A list containing individuals for the initial population.
                If none or an empty list is provided, the population will be initialized randomly
        """
        self.problem = problem
        self.mutator = mutator
        self.crossover = crossover
        self.selector = selector
        self.properties = properties

        if initial_population == None or initial_population == [] or len(initial_population) < 2:
            self.parents = self.create_population()
        else:
            self.parents = initial_population

        self.childs = []
        self.generation_count = 0

    def create_population(self):
        return [self.create_individual() for _ in range(self.properties.selection_amount)]

    def create_individual(self):
        return random.choices(self.problem.genes, k=self.problem.individuals_length)

    def run(self):
        while (self.properties.halting_generations > self.generation_count):
            self.parents = self.selector(self.parents.copy(), self.problem.fitness, self.properties)
            self.childs = [self.crossover(c1, c2) for [c1, c2] in [random.choices(self.parents, k=2) for _ in range(self.properties.selection_amount)]]
            self.childs = [self.mutator(chromosome, self.problem.genes, self.properties) for chromosome in self.childs.copy()]
            self.parents = self.childs.copy()
            self.generation_count += 1

    def get_best_individual(self):
        cmp = max if self.properties.optimization_type == "MAX" else min
        return cmp(self.childs, key=lambda x: self.problem.fitness(x))


