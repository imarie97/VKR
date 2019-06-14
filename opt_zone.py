from genetic_for_mass import ga
from visualize import vizualize

if __name__=='__main__':
    alpha = 20
    beta = 20
    gamma = 20
    limit = [1, 9, -alpha, alpha, -beta, beta, -gamma, gamma]
    crop = 500 #кол-во хромосом
    epoch = 10 #кол-во эпох
    # limit, alpha, beta, crop, epoch
    v = ga(limit, 0, 10, crop, epoch)
    vizualize(v, 'Optimal zone')
