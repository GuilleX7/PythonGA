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
                If none or an empty list is provided, the population will be initialized randomly.
                A minimum of 2 individuals are required
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
        """
        Generates a population for the problem instance using random genes. The population
        will fit the properties.selection_amount number.

        Returns:
            list<list<number>>: Initial population for the problem instance
        """
        return [self.create_individual() for _ in range(self.properties.selection_amount)]

    def create_individual(self):
        """
        Generates a single individual (chromosome) for the problem instance using random
        genes.

        Returns:
            list<number>: A single individual for the problem instance
        """
        return random.choices(self.problem.genes, k=self.problem.individuals_length)

    def is_halted(self):
        """
        Returns whether the problem has been already halted or not, this is, if
        the actual generation has reached the maximum generation count or not.

        Returns:
            boolean: Whether the actual generation has reached the maximum number
                of generations
        """
        return self.properties.halting_generations <= self.generation_count

    def calculate_next_generation(self):
        """
        Calculates the next generation of individuals. It doesn't take into account whether
        the problem instance has already halted or not, so it can calculate subsequent generations
        after finishing.
        """
        self.parents = self.selector(self.parents, self.problem.fitness, self.properties)
        self.childs = [self.crossover(c1, c2) for [c1, c2] in [random.choices(self.parents, k=2) for _ in range(self.properties.selection_amount)]]
        self.childs = [self.mutator(chromosome, self.problem.genes, self.properties) for chromosome in self.childs]
        self.parents = self.childs.copy()
        self.generation_count += 1

    def run_until_halt(self):
        """
        Runs the problem instance and calculates generation until the halting condition is met.
        """
        while not self.is_halted():
            self.calculate_next_generation()

    def get_best_individual(self):
        """
        Gets the best individual from the current generation.

        Returns:
            list<number>: Best individual in the current generation
        """
        cmp = max if self.properties.optimization_type == "MAX" else min
        return cmp(self.childs, key=lambda x: self.problem.fitness(x))

    def decode_individual(self, individual):
        """
        Auxiliary method. Decodes an individual.

        Args:
            individual (list<number>): A given individual for this problem

        Returns:
            ?: The solution after being decoded for this problem
        """
        return self.problem.decode(individual)

    def fitness_individual(self, individual):
        """
        Auxiliary method. Calculates the fitness of an individual.

        Args:
            individual (list<number>): A given individual for this problem

        Returns:
            number: The fitness of the given individual with respect to
                this problem
        """
        return self.problem.fitness(individual)


