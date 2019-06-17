import numpy as np
from itertools import product
import operator
from individual import Individual
import newton
from vector import Vector

a_par = 0.4
b_par = 0.4
c_par = 0.4

# расстояние до центра масс
def F(vc, v):
    return -(pow(vc - v, 2))

def cross(ind1, ind2, limit):
    ind1 = np.asarray(Individual.getQ(ind1))
    ind2 = np.asarray(Individual.getQ(ind2))
    c = np.random.rand()
    ch1 = c * ind1 + (1 - c) * ind2
    ch2 = c * ind2 + (1 - c) * ind1
    sol1, sol2 = newton.newton(ch1, a_par, b_par, c_par), newton.newton(ch2, a_par, b_par, c_par)
    while not sol1.constraints_satisfy(limit) & sol2.constraints_satisfy(limit):
        c = np.random.rand()
        ch1 = c * ind1 + (1 - c) * ind2
        ch2 = c * ind2 + (1 - c) * ind1
        sol1, sol2 = newton.newton(ch1, a_par, b_par, c_par), newton.newton(ch2, a_par, b_par, c_par)
    return ch1, ch2, sol1, sol2

def selection(population, cropsize):
    # последние cropsize/4 эл-тов (лучшие значения V)
    return population[:(cropsize // 4)]

def mutate_function(alpha1, beta1, alpha2, beta2, alpha3, beta3):
    def f(individual, limit):
        pow_factor = 12
        new_ind = np.copy(individual)

        for i in range(len(individual)):
            if (i == 1 | i == 2):
                alpha = alpha1
                beta = beta1
            elif (i == 3 | i == 4):
                alpha = alpha2
                beta = beta2
            else:
                alpha = alpha3
                beta = beta3

            factor = np.random.rand()
            if np.random.randint(0, 2) == 0:
                new_ind[i] -= (new_ind[i] - alpha) * factor ** pow_factor
            else:
                new_ind[i] += (beta - new_ind[i]) * factor ** pow_factor

        sol = newton.newton(new_ind, a_par, b_par, c_par)
        while not sol.constraints_satisfy(limit):
            for i in range(len(individual)):
                if (i == 1 | i == 2):
                    alpha = alpha1
                    beta = beta1
                elif (i == 3 | i == 4):
                    alpha = alpha2
                    beta = beta2
                else:
                    alpha = alpha3
                    beta = beta3
                factor = np.random.rand()
                if np.random.randint(0, 2) == 0:
                    new_ind[i] -= (new_ind[i] - alpha) * factor ** pow_factor
                else:
                    new_ind[i] += (beta - new_ind[i]) * factor ** pow_factor
            sol = newton.newton(new_ind, a_par, b_par, c_par)

        return new_ind
    return f

def center_of_mass(vs):
    sum = Vector()
    for v in vs:
        sum = sum + Individual.getSol(v)
    return  sum / len(vs)

# проверить
def center_of_mass_pop(vs):
    sum = Vector()
    for v in vs:
        sum = sum + Individual.getSol(v[0])
    return  sum / len(vs)

def crossover(population, pop_len, pcross, fit, center, limit):
    parents = list(filter(lambda individual: np.random.rand() < pcross,
                          population[:int(pop_len * pcross)]))
    parent_pairs = []
    for i, p in enumerate(parents):
        parent_pairs += list(product([p], parents[:i] + parents[i + 1:]))

    childs = []
    for p1, p2 in parent_pairs:
        # Q1, Q2
        ch1, ch2, sol1, sol2 = cross(p1[0], p2[0], limit)
        childs.append((Individual(ch1, sol1), fit(center, sol1)))
        childs.append((Individual(ch2, sol2), fit(center, sol2)))
    return childs

def mutation(childs, pmut, fit, center, limit, mutation_f):
    mutation_list = list(filter(lambda individual: np.random.rand() < pmut, childs[:int(len(childs) * pmut)]))
    for i, individual in enumerate(mutation_list):
        mutated = mutation_f(Individual.getQ(individual[0]), limit)
        sol = newton.newton(mutated, a_par, b_par, c_par)
        mutation_list[i] = (Individual(mutated, sol), fit(center, sol))
    return mutation_list

def ga(limit, alpha1, beta1, alpha2, beta2, alpha3, beta3, crop, epoch, a_p, b_p, c_p, fit = F, selection=selection, n=6):
    global a_par, b_par, c_par
    a_par, b_par, c_par = a_p, b_p, c_p

    mutation_f = mutate_function(alpha1, beta1, alpha2, beta2, alpha3, beta3)
    initial_individuals1 = []

    # формируем популяцию
    for i in range (0, crop - 1):

        individual = [np.random.uniform(low=alpha1, high=beta1) for i in range(2)]
        individual = individual + [np.random.uniform(low=alpha2, high=beta2) for i in range(2)]
        individual = individual + [np.random.uniform(low=alpha3, high=beta3) for i in range(2)]

        sys_solution = newton.newton(individual, a_par, b_par, c_par)
        while not sys_solution.constraints_satisfy(limit):
            # новый набор Q и проверка на ограничения
            individual = [np.random.uniform(low=alpha1, high=beta1) for i in range(n)]
            sys_solution = newton.newton(individual, a_par, b_par, c_par)

        initial_individuals1.append(Individual(individual, sys_solution))

    center = center_of_mass(initial_individuals1)
    population = [(x, fit(center, Individual.getSol(x))) for x in initial_individuals1]
    population.sort(key=operator.itemgetter(1))

    pcross = 0.3 #вероятность кроссинговера
    pmut = 0.5 #вероятность мутации
    iter = 0

    while iter < epoch:
        iter += 1
        print('%s epoch' % iter)
        # selection
        if len(population) >= crop:
            population = selection(population, crop)

        center = center_of_mass_pop(population)
        # print(center)
        pop_len = len(population)

        # cross
        # childs = crossover(population, pop_len, pcross, fit, center, limit)
        # mutation
        # выбираются родителькие хромосомы для мутации
        mutation_list = mutation(population, pmut, fit, center, limit, mutation_f)

        population += mutation_list
        while len(population) < crop:
            childs = crossover(population, pop_len, pcross, fit, center, limit)
            mutation_list = mutation(childs, pmut, fit, center, limit, mutation_f)
            population += mutation_list
        population.sort(key=operator.itemgetter(1))

    population.sort(key=operator.itemgetter(1))
    return population[:(crop)] #??
