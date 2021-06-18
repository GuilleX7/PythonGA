from problem.problem import Problem
from problem.problem_instance import ProblemInstance
from selectors.selectors import roulette_wheel_selector

ga_problem = Problem([0, 1], 5, lambda x: x, lambda x: sum(x) ** 2)
ga_problem_inst = ProblemInstance(ga_problem, selector=roulette_wheel_selector)
ga_problem_inst.run()
print(ga_problem_inst.get_best_individual())