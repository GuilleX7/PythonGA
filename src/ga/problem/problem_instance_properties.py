class ProblemInstanceProperties:
    """
    A class containing some parameters for a instance of a genetic problem.
    """
    def __init__(self, selection_amount, selection_pressure, mutation_probability):
        """
        Constructor for the class.

        Args:
            selection_amount (number): The amount of individuals that are passed to the next generation
                in each selection
            selection_pressure (number): In case of using a tournament selector, defines the selection
                pressure, which is the number of individuals that are selected to choose the best 
            mutation_probability (number): Probability of a chromosome to be mutated when passing from
                generation to generation
        """
        self.selection_amount = selection_amount
        self.selection_pressure = selection_pressure
        self.mutation_probability = mutation_probability