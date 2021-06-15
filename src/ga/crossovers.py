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
    crossover_point=random.randrange(1,self.individuals_length-1)
    new_chromosome_1= chromosome_a[:crossover_point] + chromosome_b[crossover_point:] 
    new_chromosome_2= chromosome_b[:crossover_point] + chromosome_a[crossover_point:] 
    return [new_chromosome_1,new_chromosome_2]

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
    crossover_point_1=random.randrange(1,self.individuals_length-1)
    crossover_point_2=random.randrange(1,self.individuals_length-1)
    crossover_point_3=random.randrange(1,self.individuals_length-1)
    if(crossover_point_1==crossover_point_2 && crossover_point_2==crossover_point_3):
        new_chromosome_1= chromosome_a[:crossover_point_1] + chromosome_b[crossover_point_1:] 
        new_chromosome_2= chromosome_b[:crossover_point_1] + chromosome_a[crossover_point_1:] 
    elif(crossover_point_1<crossover_point_2 && crossover_point_1<crossover_point_3):
        if(crossover_point_2<crossover_point_3):
            new_chromosome_1= chromosome_a[:crossover_point_1] + chromosome_b[crossover_point_1:crossover_point_2]
         + chromosome_a[crossover_point_2:crossover_point_3]  + chromosome_b[crossover_point_3:]  
        new_chromosome_2= chromosome_b[:crossover_point_1] + chromosome_a[crossover_point_1:crossover_point_2]
         + chromosome_b[crossover_point_2:crossover_point_3]  + chromosome_a[crossover_point_3:]
         else:
             new_chromosome_1= chromosome_a[:crossover_point_1] + chromosome_b[crossover_point_1:crossover_point_3]
         + chromosome_a[crossover_point_3:crossover_point_2]  + chromosome_b[crossover_point_2:]  
        new_chromosome_2= chromosome_b[:crossover_point_1] + chromosome_a[crossover_point_1:crossover_point_3]
         + chromosome_b[crossover_point_3:crossover_point_2]  + chromosome_a[crossover_point_2:]
    elif(crossover_point_2<crossover_point_1 && crossover_point_2<crossover_point_3):
        if(crossover_point_1<crossover_point_3):
            new_chromosome_1= chromosome_a[:crossover_point_2] + chromosome_b[crossover_point_2:crossover_point_1]
         + chromosome_a[crossover_point_1:crossover_point_3]  + chromosome_b[crossover_point_3:]  
        new_chromosome_2= chromosome_b[:crossover_point_2] + chromosome_a[crossover_point_2:crossover_point_1]
         + chromosome_b[crossover_point_1:crossover_point_3]  + chromosome_a[crossover_point_3:]
         else:
             new_chromosome_1= chromosome_a[:crossover_point_2] + chromosome_b[crossover_point_2:crossover_point_3]
         + chromosome_a[crossover_point_3:crossover_point_1]  + chromosome_b[crossover_point_1:]  
        new_chromosome_2= chromosome_b[:crossover_point_2] + chromosome_a[crossover_point_2:crossover_point_3]
         + chromosome_b[crossover_point_3:crossover_point_1]  + chromosome_a[crossover_point_1:] 
    elif(crossover_point_3<crossover_point_1 && crossover_point_3<crossover_point_2):
        if(crossover_point_1<crossover_point_2):
            new_chromosome_1= chromosome_a[:crossover_point_3] + chromosome_b[crossover_point_3:crossover_point_1]
         + chromosome_a[crossover_point_1:crossover_point_2]  + chromosome_b[crossover_point_2:]  
        new_chromosome_2= chromosome_b[:crossover_point_3] + chromosome_a[crossover_point_3:crossover_point_1]
         + chromosome_b[crossover_point_1:crossover_point_2]  + chromosome_a[crossover_point_2:]
         else:
             new_chromosome_1= chromosome_a[:crossover_point_3] + chromosome_b[crossover_point_3:crossover_point_2]
         + chromosome_a[crossover_point_2:crossover_point_1]  + chromosome_b[crossover_point_1:]  
        new_chromosome_2= chromosome_b[:crossover_point_3] + chromosome_a[crossover_point_3:crossover_point_2]
         + chromosome_b[crossover_point_2:crossover_point_1]  + chromosome_a[crossover_point_1:]   

    
    return [new_chromosome_1,new_chromosome_2]

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
