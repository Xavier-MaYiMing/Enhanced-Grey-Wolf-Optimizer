#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/21 15:09
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : EGWO.py
# @Statement : Enhanced Grey Wolf Optimizer
# @Reference : Kaiping Luo. Enhanced grey wolf optimizer with a model for dynamically estimating the location of the prey. Applied Soft Computing. 2019,77 :225-235.
import random
import math
import matplotlib.pyplot as plt


def obj(x):
    """
    The objective function of pressure vessel design
    :param x:
    :return:
    """
    x1 = x[0]
    x2 = x[1]
    x3 = x[2]
    x4 = x[3]
    g1 = -x1 + 0.0193 * x3
    g2 = -x2 + 0.00954 * x3
    g3 = -math.pi * x3 ** 2 - 4 * math.pi * x3 ** 3 / 3 + 1296000
    g4 = x4 - 240
    if g1 <= 0 and g2 <= 0 and g3 <= 0 and g4 <= 0:
        return 0.6224 * x1 * x3 * x4 + 1.7781 * x2 * x3 ** 2 + 3.1661 * x1 ** 2 * x4 + 19.84 * x1 ** 2 * x3
    else:
        return 1e10


def main(pop, iter, lb, ub):
    """
    The main function of EGWO
    :param pop: the number of wolves
    :param iter: the iteration number
    :param lb: the lower bound (list)
    :param ub: the upper bound (list)
    :return:
    """
    # Step 1. Initialization
    dim = len(lb)  # dimension
    pos = []  # the position of wolves
    score = []  # the score of wolves
    iter_best = []  # the best-so-far score of each iteration
    for _ in range(pop):
        temp_pos = [random.uniform(lb[i], ub[i]) for i in range(dim)]
        pos.append(temp_pos)
        score.append(obj(temp_pos))
    sorted_score = sorted(score)
    alpha_score = sorted_score[0]  # the score of the alpha wolf
    beta_score = sorted_score[1]  # the score of the beta wolf
    delta_score = sorted_score[2]  # the score of the delta wolf
    alpha_pos = pos[score.index(alpha_score)].copy()  # the position of the alpha wolf
    beta_pos = pos[score.index(beta_score)].copy()  # the position of the beta wolf
    delta_pos = pos[score.index(delta_score)].copy()  # the position of the delta wolf
    gbest = alpha_score  # the global best score
    gbest_pos = alpha_pos.copy()  # the global best position
    con_iter = 0

    # Step 2. The main loop
    for t in range(iter):

        # Step 2.1. Update the prey
        temp_weight = [random.uniform(1, 3) for _ in range(3)]
        temp_weight = sorted(temp_weight, reverse=True)
        sum_weight = sum(temp_weight)
        omega = [temp_weight[i] / sum_weight for i in range(3)]
        std = math.exp(-100 * (t + 1) / iter)  # the standard deviation of the simulated stochastic error
        prey_pos = [omega[0] * alpha_pos[i] + omega[1] * beta_pos[i] + omega[2] * delta_pos[i] + random.normalvariate(0, std) for i in range(dim)] 

        # Step 2.2. Update the position of all wolves
        for i in range(pop):
            for j in range(dim):
                y = prey_pos[j] - random.uniform(-2, 2) * abs(prey_pos[j] - pos[i][j])
                if y > ub[j]:
                    pos[i][j] = pos[i][j] + random.random() * (ub[j] - pos[i][j])
                elif y < lb[j]:
                    pos[i][j] = pos[i][j] + random.random() * (lb[j] - pos[i][j])
                else:
                    pos[i][j] = y
            
            # Step 2.3. Update alpha, beta, and delta wolves
            score[i] = obj(pos[i])
            if score[i] < alpha_score:
                alpha_score = score[i]
                alpha_pos = pos[i].copy()
            elif score[i] < beta_score:
                beta_score = score[i]
                beta_pos = pos[i].copy()
            elif score[i] < delta_score:
                delta_score = score[i]
                delta_pos = pos[i].copy()

            # Step 2.4. Update the global best
            if score[i] < gbest:
                gbest = score[i]
                gbest_pos = pos[i].copy()
                con_iter = t + 1
        iter_best.append(gbest)

    # Step 3. Sort the results
    x = [i for i in range(iter)]
    plt.figure()
    plt.plot(x, iter_best, linewidth=2, color='blue')
    plt.xlabel('Iteration number')
    plt.ylabel('Global optimal value')
    plt.title('Convergence curve')
    plt.show()
    return {'best score': gbest, 'best solution': gbest_pos, 'convergence iteration': con_iter}


if __name__ == '__main__':
    # Parameter settings
    pop = 50
    iter = 2000
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    print(main(pop, iter, lb, ub))
