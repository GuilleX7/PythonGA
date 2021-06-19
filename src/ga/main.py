from math import sin
from multiknapsack.multiknapsack_problem import MultiknapsackProblem
from crossovers.crossovers import single_point_crossover, triple_point_crossover, uniform_crossover
import io
import random

def calculate_best_balanced_distribution(objects, n_min, n_max):
    """
    Calculates the best distribution of the given objects in a given
    amount of knapsacks in the range [n_min, n_max]. It returns a list with
    both the best individual found and the n for which the problem has been
    calculated.

    Args:
        objects (list<number>): A list with the objects to be distributed
        n_min (number): The minimum amount of knapsacks for the objects to be distributed into
        n_max (number): The maximum amount of knapsakcs for the objects to be distributed into

    Returns:
        tuple<list<number>, number>: A tuple containing the best individual found in first place
            and the number of knapsacks of the problem in second place
    """
    with io.open("./reports/best_balanced_distribution_summary.txt", "w") as summary_file:
        mk_problems = [MultiknapsackProblem(objects, n) for n in range(n_min, n_max + 1)]
        mk_solutions = []
        for i, mk_problem in enumerate(mk_problems):
            mk_problem.problem_instance.properties.selection_amount = 500
            mk_problem.problem_instance.properties.mutation_probability = 0.05
            mk_problem.run()
            winner = mk_problem.problem_instance.get_best_individual()
            solution = mk_problem.get_solution()
            with io.open("./reports/best_balanced_distribution_n_" + str(i + n_min) + ".txt", "w", encoding="utf-8") as individual_report_file:
                individual_report_file.write(mk_problem.get_pretty_solution())
            
            summary_file.write("Found solution for n=" + str(i + n_min) + ": knapsacks " + str(solution[0]) + " with distance to perfection " + str(solution[1]) + "\n")
            print("Found solution for n=" + str(i + n_min) + ": knapsacks " + str(solution[0]) + " with distance to perfection " + str(solution[1]))
            
            mk_solutions.append([i, winner, solution[1]])
        
        best_solution = min(mk_solutions, key=lambda x: x[2])
        
        summary_file.write("=============================\nBEST solution is n=" + str(best_solution[0] + n_min))
        print("=============================\nBEST solution is n=" + str(best_solution[0] + n_min))
        
        return [best_solution[1], best_solution[0]]

def experiment_distributions(objects, knapsack_amount, conditions):
    """
    Allows to run instances of the same problem under different conditions.

    Args:
        objects (): [description]
        conditions (list<dict<string, ?>>): A list containing dictionaries with the following problem properties:
            selection_amount, mutation_probability, halting_generations, crossover
    """
    with io.open("./reports/experiment_summary.txt", "w") as summary_file:
        mk_problems = [MultiknapsackProblem(objects, knapsack_amount) for _ in range(len(conditions))]
        for i, mk_problem in enumerate(mk_problems):
            mk_problem.problem_instance.properties.selection_amount = conditions[i]["selection_amount"]
            mk_problem.problem_instance.properties.mutation_probability = conditions[i]["mutation_probability"]
            mk_problem.problem_instance.properties.halting_generations = conditions[i]["halting_generations"]
            mk_problem.problem_instance.crossover = conditions[i]["crossover"]
            mk_problem.run()
            solution = mk_problem.get_solution()
            with io.open("./reports/experiment_distribution_" + str(i) + ".txt", "w", encoding="utf-8") as individual_report_file:
                individual_report_file.write("Selection amount: " + str(conditions[i]["selection_amount"]) + "\n")
                individual_report_file.write("Mutation probability [0, 1]: " + str(conditions[i]["mutation_probability"]) + "\n")
                individual_report_file.write("Halting amount of generations: " + str(conditions[i]["halting_generations"]) + "\n")
                individual_report_file.write("Crossover function: " + str(conditions[i]["crossover"]) + "\n\n")
                individual_report_file.write(mk_problem.get_pretty_solution())
            print("\nEXPERIMENT " + str(i))
            print("Selection amount: " + str(conditions[i]["selection_amount"]))
            print("Mutation probability [0, 1]: " + str(conditions[i]["mutation_probability"]))
            print("Halting amount of generations: " + str(conditions[i]["halting_generations"]))
            print("Crossover function: " + str(conditions[i]["crossover"]))
            
            summary_file.write("Experiment " + str(i) + ": knapsacks " + str(solution[0]) + " with distance to perfection " + str(solution[1]) + "\n")
            print("Result: knapsacks " + str(solution[0]) + " with distance to perfection " + str(solution[1]))

# MAIN PROGRAM
# 1. First, we try to distribute a list of random objects in a given number of knapsacks, n, in a range between 2 and 10
#print("1. DISTRIBUTION OF RANDOM OBJECTS IN A RANGE 'n' OF KNAPSACKS")
#num_objects = random.randint(100, 200)
#print("Selected amount of objects: " + str(num_objects))
#calculate_best_balanced_distribution([random.randint(1, 100) for _ in range(num_objects)], 2, 10)

# 2. We perform some experiments using different properties for each instance of the problem
print("\n2. EXPERIMENTS")
num_objects = random.randint(1000, 1500)
print("Selected amount of objects: " + str(num_objects))
experiment_distributions(
    [random.randint(1, 100) for _ in range(num_objects)],
    4,
    [
        {"selection_amount": 100, "mutation_probability": 0.05, "halting_generations": 100, "crossover": single_point_crossover},
        {"selection_amount": 300, "mutation_probability": 0.05, "halting_generations": 300, "crossover": triple_point_crossover},
    ]
)