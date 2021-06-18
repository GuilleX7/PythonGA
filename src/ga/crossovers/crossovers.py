import random


def single_point_crossover(chromosome_a, chromosome_b):
    """
    Performs a single point crossover over two chromosomes.

    A random crossover point is chosen, so all the genes before
    the point are inherited from first chromosome, while all the
    genes after the crossover point are inherited from the second
    chromosome.

    The chromosome length must be at least 2 genes long.

    Args:
        chromosome_a (list<number>): First chromosome
        chromosome_b (list<number>): Second chromosome
    """
    crossover_point = random.randrange(1, len(chromosome_a))
    new_chromosome = chromosome_a[:crossover_point] + chromosome_b[crossover_point:]
    return new_chromosome


def triple_point_crossover(chromosome_a, chromosome_b):
    """
    Performs a multiple point crossover with three crossover points
    over two chromosomes.

    Three crossover points are calculated, so the even segments of
    genes will be inherited from the first chromosome, while the
    odd segments of genes will be inherited from the second chromosome.

    The chromosome length must be at least 6 genes long.

    Args:
        chromosome_a (list<number>): First chromosome
        chromosome_b (list<number>): Second chromosome
    """
    chromosome_length = len(chromosome_a)
    chromosome_length_third = chromosome_length // 3
    crossover_point_1 = random.randrange(1, chromosome_length_third)
    crossover_point_2 = random.randrange(chromosome_length_third, 2 * chromosome_length_third)
    crossover_point_3 = random.randrange(2 * chromosome_length_third, chromosome_length)
    new_chromosome = chromosome_a[:crossover_point_1] + chromosome_b[crossover_point_1:crossover_point_2] + chromosome_a[crossover_point_2:crossover_point_3] + chromosome_b[crossover_point_3:]
    return new_chromosome


def uniform_crossover(chromosome_a, chromosome_b):
    """
    Performs a uniform crossover over two chromosomes.

    Each gene is chosen randomly either from the first
    chromosome or from the second one.

    The chromosome length can be whatever.

    Args:
        chromosome_a (list<number>): First chromosome
        chromosome_b (list<number>): Second chromosome
    """
    return [chromosome_a[i] if random.randint(0, 1) == 0 else chromosome_b[i] for i in range(len(chromosome_a))]
