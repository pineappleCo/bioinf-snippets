
def expGrow(steps, born):
    pop = [1, 1]
    for x in xrange(2, steps):
        nextPop = (pop[x - 2] * born) + pop[x - 1]
        pop.append(nextPop)
    return pop[len(pop) - 1]

def expMortalGrow(steps, born, lifespan):
    pop = [1, 1]
    for x in xrange(2, steps):
        nextPop = (pop[x - 2] * born) + pop[x - 1]
        pop.append(nextPop)
    return pop[len(pop) - 1] - pop[len(pop) - (lifespan + 1)]

