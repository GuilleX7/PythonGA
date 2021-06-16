class ProblemInstance:
    """
    Class that represents an instantiated genetic problem, containing
    everything related with the populations and the mutation and crossover
    mechanisms.
    """
    def __init__(self, problem, initial_population, mutator, crossover, selector, properties):
        """
        Constructor for the class.

        Args:
            problem (Problem): Genetic problem
            initial_population (list<number>): A list containing individuals for the initial population.
                If none or an empty list is provided, the population will be initialized randomly
            mutator (function): Mutator function used for the chromosome mutations
            crossover (function): Crossover function used for performing crossover over two individuals 
            selector (function): Selection function used in order to select the individuals for the next
                generation
            properties (ProblemInstanceProperties): Contains the specific properties used in this instance
                of the problem
        """
        self.problem = problem
        self.initial_population = initial_population
        self.mutator = mutator
        self.crossover = crossover
        self.selector = selector
        self.properties = properties

        