import random
from collections import namedtuple
from crossovers.crossovers import triple_point_crossover, uniform_crossover
from problem.problem import Problem
from problem.problem_instance import ProblemInstance
from selectors.selectors import roulette_wheel_selector, tournament_selector

num_objects = 20
object_min_weight = 1
object_max_weight = 100
num_knaps = 5
knap_min_space = 1
knap_max_space = 150

KnapObject = namedtuple("KnapObject", "weight")

objects = [KnapObject(random.randint(object_min_weight, object_max_weight)) for _ in range(num_objects)]
knap_available_spaces = [random.randint(knap_min_space, knap_max_space) for _ in range(num_knaps)]


def knap_decode(chromosome):
    knaps_spaces = [0] * num_knaps
    difference = 0
    penalty = 0
    for i, selected_knap in enumerate(chromosome):
        if selected_knap == -1:
            continue
        knaps_spaces[selected_knap] += objects[i].weight
        if knaps_spaces[selected_knap] > knap_available_spaces[selected_knap]:
            penalty += objects[i].weight

    for i in range(0, num_knaps - 1):
        difference += abs(knaps_spaces[i] - knaps_spaces[i + 1])

    return [knaps_spaces, difference, penalty]


def knap_fitness(chromosome):
    knaps_spaces = [0] * num_knaps
    difference = 0
    penalty = 0
    for i, selected_knap in enumerate(chromosome):
        if selected_knap == -1:
            continue
        knaps_spaces[selected_knap] += objects[i].weight
        if knaps_spaces[selected_knap] > knap_available_spaces[selected_knap]:
            penalty += objects[i].weight

    for i in range(0, num_knaps - 1):
        difference += abs(knaps_spaces[i] - knaps_spaces[i + 1])

    return difference + penalty * 100


ga_problem = Problem(list(range(-1, num_knaps)), num_objects, knap_decode, knap_fitness)
ga_problem_inst = ProblemInstance(ga_problem)
ga_problem_inst.properties.optimization_type = "MIN"
ga_problem_inst.properties.mutation_probability = 0.2

while not ga_problem_inst.is_halted():
    ga_problem_inst.calculate_next_generation()
    print("Best individual of generation " + str(ga_problem_inst.generation_count) + ": " + str(ga_problem_inst.decode_individual(ga_problem_inst.get_best_individual())))

winner = ga_problem_inst.get_best_individual()
print("Spaces available: " + str(knap_available_spaces))
print("Best solution found: " + str(ga_problem_inst.decode_individual(winner)))
