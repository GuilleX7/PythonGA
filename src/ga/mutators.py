def simple_mutator(self,chromosome,probability):
    """
    Changes some genes with a given probability.

    Args:
        chromosome (list<number>): chromosome to be mutated
        probability (number): mutation probability
    """
    mutated_chromosome=list(chromosome) 
        for i in range(len(chromosome)):
            if random.random() < probability :
                mutated_chromosome[i] = random.choice(self.genes)
        return mutated_chromosome
