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

def find_solution_points_for_point_slope(point, slope, start = -100, end = 100):
    integers = [x for x in range(start, end + 1)]
    solution_points = []
    for x in integers:
        for y in integers:
            try:
                if (y - (point[1]) == slope * (x - point[0])):
                    # print(f'({x}, {y})')
                    solution_points.append([x, y])
            except Exception as e:
                pass
    print('Solution points for ' + color(equation, 'blue') + f': {solution_points}')
    check_for_symmetry(solution_points)
    return solution_points
