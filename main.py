import math
import numpy as np                   
from matplotlib import pyplot as plt
import itertools

def plot_points(points):
    data = np.array(points)
    x, y = data.T
    plt.plot(x, y, '-go')
    plt.show()

def find_solution_points(start, end):
    integers = [x for x in range(start, end + 1)]
    solution_points = []
    for x in integers:
        for y in integers:
            # Replace with desired equation
            # todo: pass equation in as parameter
            if (y == 2 * (-x) ** 3 - (-x)):
                # print(f'({x}, {y})')
                solution_points.append([x, y])
    print('Solution points: ', solution_points)
    plot_points(solution_points)
    return solution_points
    
solution_points = find_solution_points(-10000, 10000)

def find_intercepts(points):
    intercepts = []
    for point in points:
        if 0 in point:
            # print(point)
            intercepts.append(point)
    print('Intercepts: ', intercepts)
    return intercepts

find_intercepts(solution_points)

def generate_mirrors_from_intercepts(points):
    # todo
    return

generate_mirrors_from_intercepts(solution_points)

# finds x-Axis, y-Axis, and origin symmetry 
def find_symmetry(points):
    # todo
    return
