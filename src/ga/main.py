from multiknapsack.multiknapsack_problem import MultiknapsackProblem
import io

mk_problem = MultiknapsackProblem.of_random_objects(50, 1, 100, 5)
mk_problem.run()
with io.open("dog_breeds.txt", mode="w", encoding="utf-8") as f:
    f.write(mk_problem.get_detailed_solution())