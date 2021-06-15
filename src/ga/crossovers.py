def single_point_crossover(chromosome_a, chromosome_b):
    """
    Performs a single point crossover over two chromosomes.

    A random crossover point is chosen, so all the genes before
    the point are inherited from first chromosome, while all the
    genes after the crossover point are inherited from the second
    chromosome.

    Args:
        chromosome_a (list<number>): First chromosome
        chromosome_b (list<number>): Second chromosome
    """
    pass

def triple_point_crossover(chromosome_a, chromosome_b):
    """
    Performs a multiple point crossover with three crossover points
    over two chromosomes.

    Three crossover points are calculated, so the even segments of
    genes will be inherited from the first chromosome, while the
    odd segments of genes will be inherited from the second chromosome.

    Args:
        chromosome_a (list<number>): First chromosome
        chromosome_b (list<number>): Second chromosome
    """
    pass

def uniform_crossover(chromosome_a, chromosome_b):
    """
    Performs a uniform crossover over two chromosomes.

    Each gene is chosen randomly either from the first
    chromosome or from the second one.

    Args:
        chromosome_a (list<number>): First chromosome
        chromosome_b (list<number>): Second chromosome
    """
    pass
