import random
from collections import namedtuple
from typing import final
from crossovers.crossovers import triple_point_crossover, uniform_crossover
from problem.problem import Problem
from problem.problem_instance import ProblemInstance
from selectors.selectors import roulette_wheel_selector, tournament_selector

num_objects = 50
object_min_weight = 1
object_max_weight = 100
num_knaps = 2

objects = [random.randint(object_min_weight, object_max_weight) for _ in range(num_objects)]
perfect_average_weight = sum(objects) / num_knaps


def knap_decode(chromosome):
    knaps = [[] for _ in range(num_knaps)]
    for i, selected_knap in enumerate(chromosome):
        knaps[selected_knap].append(i)
    return knaps


def knap_fitness(chromosome):
    knaps_spaces = [0] * num_knaps
    for i, selected_knap in enumerate(chromosome):
        knaps_spaces[selected_knap] += objects[i]
    distance_from_perfect_weight = sum([abs(knaps_spaces[i] - perfect_average_weight) ** 2 for i in range(num_knaps)])
    return distance_from_perfect_weight


ga_problem = Problem(list(range(num_knaps)), num_objects, knap_decode, knap_fitness)
ga_problem_inst = ProblemInstance(ga_problem)
ga_problem_inst.properties.optimization_type = "MIN"
ga_problem_inst.properties.mutation_probability = 0.1

while not ga_problem_inst.is_halted():
    ga_problem_inst.calculate_next_generation()
    best = ga_problem_inst.get_best_individual()
    print("Best individual of generation " + str(ga_problem_inst.generation_count) + ": " + str(ga_problem_inst.decode_individual(best)) + " with fitness " + str(ga_problem_inst.fitness_individual(best)))

print("=====================================================")
winner = ga_problem_inst.get_best_individual()
final_knaps = ga_problem_inst.decode_individual(winner)
final_spaces = []
for i, knap in enumerate(final_knaps):
    print("KNAP Nº" + str(i + 1))
    total_knap_weight = 0
    for i in knap:
        print("Object nº" + str(i + 1) + " with weight " + str(objects[i]))
        total_knap_weight += objects[i]
    final_spaces.append(total_knap_weight)
    print("Total weight: " + str(total_knap_weight) + "\n")

print("Perfect average weight: " + str(perfect_average_weight) + ", obtained: " + str(final_spaces) + " with distance (fitness): " + str(ga_problem_inst.fitness_individual(winner)))