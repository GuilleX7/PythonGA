import random

from problem.problem import Problem
from problem.problem_instance import ProblemInstance


class MultiknapsackProblem:
    def __init__(self, objects, knapsack_amount):
        self.objects = objects
        self.knapsack_number = knapsack_amount
        self.perfect_average_weight = sum(objects) / knapsack_amount

        self.problem = Problem(list(range(knapsack_amount)), len(objects), self.decode, self.fitness)
        self.problem_instance = ProblemInstance(self.problem)
        self.problem_instance.properties.optimization_type = "MIN"
        self.problem_instance.properties.mutation_probability = 0.1

    @staticmethod
    def of_random_objects(object_amount, min_weight, max_weight, knapsack_amount):
        return MultiknapsackProblem([random.randint(min_weight, max_weight) for _ in range(object_amount)], knapsack_amount)

    def decode(self, chromosome):
        knaps = [[] for _ in range(self.knapsack_number)]
        for i, selected_knap in enumerate(chromosome):
            knaps[selected_knap].append(i)
        return knaps

    def fitness(self, chromosome):
        knaps_spaces = [0] * self.knapsack_number
        for i, selected_knap in enumerate(chromosome):
            knaps_spaces[selected_knap] += self.objects[i]
        distance_from_perfect_weight = sum([abs(knaps_spaces[i] - self.perfect_average_weight) ** 2 for i in range(self.knapsack_number)])
        return distance_from_perfect_weight

    def run(self):
        self.problem_instance.run_until_halt()

    def get_detailed_solution(self):
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
