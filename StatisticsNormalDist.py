
"""
f(x, mu = 0, sigma = 1) = 1/(sqrt(2*pi*sigma**2))(-.5(exp**((x-mu)/sigma)**2))
"""

# normal distribution function

import math
import random
import matplotlib.pyplot as plt

def norm_first_part(sigma = 1):
    denominator = math.sqrt(2*(math.pi)*(math.pow(sigma, 2)))
    return 1/denominator

def norm_last_part(x, mu = 0, sigma = 1):
    numerator = math.pow(((x-mu)/sigma), 2)
    denominator = -2
    return numerator/denominator

def mean(x):
    total = 0
    for i in x:
        total += i
    return total/len(x)

def sum_of_square(x):
    total = 0
    for i in x:
        total += math.pow(i, 2)
    return total

def de_mean(x):
    mu = mean(x)
    return [(i-mu) for i in x]

def variance(x):
    return sum_of_square(de_mean(x))/(len(x)-1)


def normal_distribution(x, mu=0, sigma=1):
    value = norm_first_part(sigma)*math.exp(norm_last_part(x, mu, sigma))
    return value

dataset = [random.randint(10, 30) for _ in range(100)]

normal_mean = mean(dataset)
normal_variance = variance(dataset)

x_i = [normal_distribution(x, normal_mean, normal_variance) for x in dataset]

plt.plot(dataset, x_i, linestyle='-')
    
    
    