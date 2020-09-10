import math
import numpy as np                   
from matplotlib import pyplot as plt
import itertools

intercept_symmetry_map = {
    'x_intercept': 'x-Axis',
    'y_intercept': 'y-Axis'
}

def plot_points(points):
    data = np.array(points)
    x, y = data.T
    plt.plot(x, y, 'go')
    plt.show()


def find_solution_points(equation, start, end):
    integers = [x for x in range(start, end + 1)]
    solution_points = []
    for x in integers:
        for y in integers:
            if (eval(equation)):
                # print(f'({x}, {y})')
                solution_points.append([x, y])
    print('Solution points: ', solution_points)
    return solution_points
    

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
        return 'origin_symmetry'
    if (intercept[0] == 0 and intercept[1] != 0):
        return 'y_intercept'
    if (intercept[0] != 0 and intercept[1] == 0):
        return 'x_intercept'


# finds x-Axis, y-Axis, and origin symmetry 
def find_symmetry(points):
    # todo:
    # find intercpets
    # check for orgin symmetry
    # check for y-Axis symmetry
    # check for x-Axis symmetry
    return


# The points passed in must be either before or after an intercept, intercept exclusive.
def add_symmetry(points, intercept, symmetry):
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

        intercept_type = find_intercept_type(intercept)

        if (not intercept_type):
            raise Exception('No intercept type found')

        print('Intercept type: ', intercept_type)

        if (len(sequence_before_intercept) == 0):
            print('No points found before intercept, exiting')
            return []

        augemented_sequence_1 = add_symmetry(sequence_before_intercept, intercept, intercept_symmetry_map[intercept_type])
        # augemented_sequence_2 = add_symmetry(sequence_after_intercept, intercept, intercept_symmetry_map[intercept_type])

        mirrors_from_intercept = {
            'intercept': intercept,
            'mirror1': augemented_sequence_1,
            # 'mirror2': augemented_sequence_2
        }

        augmented_sequences.append(mirrors_from_intercept)

    print(augmented_sequences)
    return augmented_sequences


####### Tests (todo: move and expand into pytest file)
solution_points = find_solution_points('x - y ** 2 == 1', -100, 100)
plot_points(solution_points)

mirrored_sequences = generate_mirrors_from_intercepts(solution_points)
for mirror in mirrored_sequences:
    plot_points(mirror['mirror1'])
