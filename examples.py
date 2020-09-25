import random
from main import *

# Illustrates how to create graphs with a common intersection. Here all graphs intersect at point (-1, 4)
def plot_intersecting_randomness(number_of_graphs = 10, int_range = [-10, 10]):
    integers = [x for x in range(int_range[0], int_range[1] + 1)]
    graphs = []
    for i in range(number_of_graphs):
        graphs.append(f'y - 4 == {random.choice(integers)} * (x + 1)')
    print('Graphs: ', graphs)
    find_intersections(graphs, [], True)


# Demonstrates how when the x- and y-axes have different units of measure
# the slope becomes a rate or a rate of change. When the units of measure are the 
# sane the slope is a ratio.
def calculate_population_growth(point_a, point_b):
    growth_rate = calculate_slope(point_a, point_b)
    # print(f'Population in this region is growing at {growth_rate} people per year')
    return growth_rate

# In this example the population of an imaginary region was 2,717,000 in 1980 and 
# 3,665,000 in 1990. The years are measured on the x-axis and the population
# is measured on the y-axis. (Recall that slope = change_in(y)/change_in(x)).
# The growth rate for this time is 94800 people per year.
# calculate_population_growth([1980, 2717000], [1990, 3665000])

# Using real world data: the population of the USA in 2010 was some 309,300,000 souls.
# In 2020 it is estimated to be about 331,000,000 (pending the 2020 census, prior to high stakes election,
# in the midst of a pandemic, huzzah :| ). The growth rate for this time is 2,170,000 people per year.
# calculate_population_growth([2010, 309300000], [2020, 331000000])
