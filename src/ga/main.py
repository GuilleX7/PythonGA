import selectors.selectors as selectors

chromosomes = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [1, 1, 1]]
fitness = lambda x: sum(x) ** 2
properties = dict()
properties["amount"] = 1

print(selectors.roulette_wheel_selector(chromosomes, fitness, properties))