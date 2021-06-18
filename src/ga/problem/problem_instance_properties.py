class ProblemInstanceProperties:
    """
    A class containing some parameters for a instance of a genetic problem.
    """
    def __init__(self, optimization_type="MAX", halting_generations=100, selection_amount=500, selection_pressure=50, mutation_probability=0.05):
        """
        Constructor for the class.

        Args:
            optimization_type (string): Can take the values "MIN" or "MAX", depending whether the problem
            halting_generations (number): Number of generations after the algorithm will stop executing
            selection_amount (number): The amount of individuals that are passed to the next generation
                in each selection
            selection_pressure (number): In case of using a tournament selector, defines the selection
                pressure, which is the number of individuals that are selected to choose the best 
            mutation_probability (number): Probability of a chromosome to be mutated when passing from
                generation to generation
        """
        if optimization_type != "MIN" and optimization_type != "MAX":
            self.optimization_type = "MAX"
        else:
            self.optimization_type = optimization_type

        self.halting_generations = halting_generations
        self.selection_amount = selection_amount
        self.selection_pressure = selection_pressure
        self.mutation_probability = mutation_probability