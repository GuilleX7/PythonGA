import random

from problem.problem import Problem
from problem.problem_instance import ProblemInstance


class MultiknapsackProblem:
    def __init__(self, objects, knapsack_amount):
        """
        Creates a Multiknapsack Problem instance with a given list of objects and
        a given knapsack amount.

        Args:
            objects (list<number>): List of objects (weights)
            knapsack_amount (number): Amount of knapsacks
        """
        self.objects = objects
        self.knapsack_number = knapsack_amount
        self.perfect_average_weight = sum(objects) / knapsack_amount

        self.problem = Problem(list(range(knapsack_amount)), len(objects), self.decode, self.fitness)
        self.problem_instance = ProblemInstance(self.problem)
        self.problem_instance.properties.optimization_type = "MIN"

    @staticmethod
    def of_random_objects(object_amount, min_weight, max_weight, knapsack_amount):
        """
        Creates a new Multiknapsack Problem with a random list of objects using
        the given parameters.

        Args:
            object_amount (number): Amount of objects
            min_weight (number): Minimum weight of an object
            max_weight (number): Maximum weight of an object
            knapsack_amount (number): Amount of knapsacks

        Returns:
            MultiknapsackProblem: The created instance
        """
        return MultiknapsackProblem([random.randint(min_weight, max_weight) for _ in range(object_amount)], knapsack_amount)

    def decode(self, chromosome):
        """
        Decodes the given solution to the problem

        Args:
            chromosome (list<number>): The individual to be decoded

        Returns:
            list<list<number>>: A list of lists, each representing a knapsack, with the indices of
                the objects that are inside them 
        """
        knaps = [[] for _ in range(self.knapsack_number)]
        for i, selected_knap in enumerate(chromosome):
            knaps[selected_knap].append(i)
        return knaps

    def fitness(self, chromosome):
        """
        Calculates the fitness of a given individual as the squared distance to
        the arithmetic mean.

        Args:
            chromosome (list<number>): The individual to be fitnessed

        Returns:
            number: The fitness of the individual
        """
        knaps_spaces = [0] * self.knapsack_number
        for i, selected_knap in enumerate(chromosome):
            knaps_spaces[selected_knap] += self.objects[i]
        distance_from_perfect_weight = sum([abs(knaps_spaces[i] - self.perfect_average_weight) ** 2 for i in range(self.knapsack_number)])
        return distance_from_perfect_weight

    def run(self):
        """
        Runs the problem until it halts.
        """
        self.problem_instance.run_until_halt()

    def get_solution(self):
        """
        Gets the best solution found after the problem is halted.

        Returns:
            tuple<list<number>, number>: A list containing in first place a list with the spaces
                occupied in each knapsack, and the fitness of the individual for which the solution
                was calculated from.
        """
        winner = self.problem_instance.get_best_individual()
        final_knaps = self.problem_instance.decode_individual(winner)
        final_spaces = []
        for i, knap in enumerate(final_knaps):
            total_knap_weight = 0
            for i in knap:
                total_knap_weight += self.objects[i]
            final_spaces.append(total_knap_weight)
        return [final_spaces, self.problem_instance.fitness_individual(winner)]

    def get_pretty_solution(self):
        """
        Prints the solution in a pretty and human-readable way.

        Returns:
            string: The pretty-printed solution
        """
        solution = ""
        winner = self.problem_instance.get_best_individual()
        final_knaps = self.problem_instance.decode_individual(winner)
        final_spaces = []
        for i, knap in enumerate(final_knaps):
            solution += "KNAP Nº" + str(i + 1) + "\n"
            total_knap_weight = 0
            for i in knap:
                solution += "Object nº" + str(i + 1) + " with weight " + str(self.objects[i]) + "\n"
                total_knap_weight += self.objects[i]
            final_spaces.append(total_knap_weight)
            solution += "Total weight: " + str(total_knap_weight) + "\n\n"
        solution += "Perfect average weight: " + str(self.perfect_average_weight) + ", obtained: " + str(final_spaces) + \
            " with distance (fitness): " + str(self.problem_instance.fitness_individual(winner)) + "\n"
        return solution
