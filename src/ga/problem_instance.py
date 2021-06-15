class ProblemInstance:
    """
    Class that represents an instantiated genetic problem, containing
    everything related with the populations and the mutation and crossover
    mechanisms.
    """
    def __init__(self, problem, mutator, crossover, selector, parameters):
        """[summary]

        Args:
            problem ([type]): [description]
            mutator ([type]): [description]
            crossover ([type]): [description]
            selector ([type]): [description]
            parameters ([type]): [description]
        """
        self.problem = problem
        self.mutator = mutator
        self.crossover = crossover
        self.selector = selector
        self.parameters = self.parameters