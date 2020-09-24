import json
import math
import random
import itertools
import numpy as np                   
from matplotlib import pyplot as plt
from text_color import color

INTERCEPT_SYMMETRY_MAP = {
    'origin': 'origin',
    'x_intercept': 'x-Axis',
    'y_intercept': 'y-Axis'
}

def plot_points(points_array):
    plot_params = []
    graph_colors = ['b', 'r', 'c', 'y', 'm', 'k', 'g'] # todo: add more colors and read from file

    for points in points_array:
        data = np.array(points)
        x, y = data.T

        plot_params.append(x)
        plot_params.append(y)

        graph_color = random.choice(graph_colors)
        plot_params.append(f'-{graph_color}') # todo: pop value from color array

    plt.plot(*plot_params)
    plt.show()


def check_for_origin_symmetry(points, sequence_before_intercept):
    if ([0, 0] not in points):
        return False

    if (sequence_before_intercept[0][0] > 0):
        for point in sequence_before_intercept:
            if ([-point[0], -point[1]] not in points):
                return False
    else:
        for point in sequence_before_intercept:
            if ([abs(point[0]), abs(point[1])] not in points):
                return False
    return True


def check_for_x_axis_symmetry(points, sequence_before_intercept):
    if (sequence_before_intercept[0][0] > 0):
        for point in sequence_before_intercept:
            if ([point[0], -point[1]] not in points):
                return False
    else:
        for point in sequence_before_intercept:
            if ([point[0], abs(point[1])] not in points):
                return False
    return True
    

def check_for_y_axis_symmetry(points, sequence_before_intercept):
    if (sequence_before_intercept[0][0] > 0):
        for point in sequence_before_intercept:
            if ([-point[0], point[1]] not in points):
                return False
    else:
        for point in sequence_before_intercept:
            if ([abs(point[0]), point[1]] not in points):
                return False
    return True


# Checks for x-Axis, y-Axis, and origin symmetry
def check_for_symmetry(points):
    symmetry_details = {
        'origin_symmetry': None,
        'x_axis_symmetry': None,
        'y_axis_symmetry': None
    }

    intercepts = find_intercepts(points)

    if (len(intercepts) == 0):
        symmetry_details['origin_symmetry'] = False
        symmetry_details['x_axis_symmetry'] = False
        symmetry_details['y_axis_symmetry'] = False

    for intercept in intercepts:
        print('Checking symmetry for sequence with intercept: ', intercept)
        index_for_intercept = points.index(intercept)

        sequence_before_intercept = points[:index_for_intercept]
        print('Sequence before intercept: ', sequence_before_intercept)

        if (len(sequence_before_intercept) > 0):
            symmetry_details['origin_symmetry'] = check_for_origin_symmetry(points, sequence_before_intercept)
            symmetry_details['x_axis_symmetry'] = check_for_x_axis_symmetry(points, sequence_before_intercept)
            symmetry_details['y_axis_symmetry'] = check_for_y_axis_symmetry(points, sequence_before_intercept)
        else:
            symmetry_details['origin_symmetry'] = False
            symmetry_details['x_axis_symmetry'] = False
            symmetry_details['y_axis_symmetry'] = False
        
    print('Symmetry details: ', symmetry_details)
    return symmetry_details


def find_solution_points_from_graph_equation(equation, start=-100, end=100):
    integers = [x for x in range(start, end + 1)]
    solution_points = []
    for x in integers:
        for y in integers:
            try:
                if (eval(equation)):
                    # print(f'({x}, {y})')
                    solution_points.append([x, y])
            except Exception as e:
                pass
    print('Solution points for ' + color(equation, 'blue') + f': {solution_points}')
    check_for_symmetry(solution_points)
    return solution_points


def find_solution_points_from_point_slope(point, slope, start=-100, end=100):
    x1, y1 = point
    equation = f'y - ({y1}) == {slope} * (x - ({x1}))'
    return find_solution_points_from_graph_equation(equation, start, end)
    

def find_intercepts(points):
    intercepts = []
    for point in points:
        if 0 in point:
            # print(point)
            intercepts.append(point)
    print('Intercepts: ', intercepts)
    return intercepts


def find_intercept_type(intercept):
    if (intercept == [0, 0]):
        return 'origin' # effectively both x- and y-intercept
    if (intercept[0] == 0 and intercept[1] != 0):
        return 'y_intercept'
    if (intercept[0] != 0 and intercept[1] == 0):
        return 'x_intercept'


# The points passed in must be either before or after an intercept, intercept exclusive.
def mirror_sequence(points, intercept, symmetry):
    print('Symmetry type: ', symmetry)
    print('On sequence: ', points)
    print('With intercept: ', intercept)

    augemented_sequence = []
    if (symmetry == 'x-Axis'):
        if (points[0][0] > 0):
            for point in points:
                augemented_sequence.append([-point[0], point[1]])
        else:
            for point in points:
                augemented_sequence.append([abs(point[0]), point[1]])

    if (symmetry == 'y-Axis'):
        if (points[0][1] > 0):
            for point in points:
                augemented_sequence.append([point[0], -point[1]])
        else:
            for point in points:
                augemented_sequence.append([point[0], abs(point[1])])
    
    augemented_sequence.reverse()
    print('Augmented sequence: ', augemented_sequence)

    mirrored_sequence = points + [intercept] + augemented_sequence
    print('Augmented sequence: ', mirrored_sequence)

    return mirrored_sequence


def generate_mirrors_from_intercepts(points):
    print('Original sequence: ', points)
    intercepts = find_intercepts(points);
    augmented_sequences = []
    for intercept in intercepts:
        print('Generating mirror for sequence with intercept: ', intercept)
        index_for_intercept = points.index(intercept)

        sequence_before_intercept = points[:index_for_intercept]
        print('Sequence before intercept: ', sequence_before_intercept)

        # sequence_after_intercept = intercepts[index_for_intercept + 1:]
        # print('Sequence before intercept: ', sequence_after_intercept)

        if (len(sequence_before_intercept) == 0):
            print('No points found before intercept, exiting')
            augmented_sequences.append({
                intercept: intercept,
                'mirror1': []
            })

        intercept_type = find_intercept_type(intercept)
        print('Intercept type: ', intercept_type)

        if (not intercept_type):
            raise Exception('No intercept type found')

        if (intercept_type != 'origin'):
            augemented_sequence_1 = mirror_sequence(sequence_before_intercept, intercept, INTERCEPT_SYMMETRY_MAP[intercept_type])
            # augemented_sequence_2 = mirror_sequence(sequence_after_intercept, intercept, INTERCEPT_SYMMETRY_MAP[intercept_type])

            mirrors_from_intercept = {
                'intercept': intercept,
                'mirror1': augemented_sequence_1,
                # 'mirror2': augemented_sequence_2
            }

            augmented_sequences.append(mirrors_from_intercept)
        else:
            augmented_sequences.append({
                'intercept': intercept,
                'mirror1': ['origin_symmetry_mirror_not_supported_yet']
            })

    print(augmented_sequences)
    return augmented_sequences


def stringify_points(points):
    stringified_points = []
    for point in points:
        stringified_points.append(str(point))
    return stringified_points


def listify_points(points):
    listified_points = []
    for point in points:
        listified_points.append(json.loads(point))
    return listified_points


def find_intersections(graph_equations, solution_points_array = [], plot_graphs = False):
    solution_points_for_graphs = []
    if (len(solution_points_array) == 0):
        for graph in graph_equations:
            print('Finding solution points for graph: ', graph)
            graph_solution_points = find_solution_points_from_graph_equation(graph)
            solution_points_for_graphs.append(stringify_points(graph_solution_points))
    else:
        for solution_points in solution_points_array:
            solution_points_for_graphs.append(stringify_points(solution_points))

    print('Solution points for graphs: ', solution_points_for_graphs)

    intersections = set.intersection(*[set(list) for list in solution_points_for_graphs])
    print('Intersections: ', list(intersections))

    if (plot_graphs):
        normalized_points = []
        for soulution_points in solution_points_for_graphs:
            normalized_points.append(listify_points(soulution_points))

        plot_points(normalized_points)

    return listify_points(list(intersections))


def calculate_slope(point_a, point_b):
    try:
        return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
    except ZeroDivisionError:
        return None
