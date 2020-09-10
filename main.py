import math
import numpy as np                   
from matplotlib import pyplot as plt
import itertools

def plot_points(points):
    data = np.array(points)
    x, y = data.T
    plt.plot(x, y, '-g')
    plt.show()


def find_solution_points(start, end):
    integers = [x for x in range(start, end + 1)]
    solution_points = []
    for x in integers:
        for y in integers:
            # Replace with desired equation
            # todo: pass equation in as parameter
            if (y == x ** 3 - (4 * x)):
                # print(f'({x}, {y})')
                solution_points.append([x, y])
    print('Solution points: ', solution_points)
    plot_points(solution_points)
    return solution_points
    
solution_points = find_solution_points(-1000, 1000)

def find_intercepts(points):
    intercepts = []
    for point in points:
        if 0 in point:
            # print(point)
            intercepts.append(point)
    print('Intercepts: ', intercepts)
    return intercepts


def find_intercept_type(intercept):
    # todo: support origin symmetry
    if (intercept[0] == 0):
        return 'y_intercept'
    if (intercept[1] == 0):
        return 'x_intercept'
    return False


# finds x-Axis, y-Axis, and origin symmetry 
def find_symmetry(points):
    # todo
    return


# The points passed in must be either before or after an intercept, exclusive
# of the actual intercept
def augment_symmetry(points, intercept, symmetry):
    print('Symmetry type: ', symmetry)
    print('On segment: ', points)
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
    generated_mirrors = []
    for intercept in intercepts:
        print('Intercept: ', intercept)
        index_for_intercept = points.index(intercept)
        sequence_before_intercept = points[:index_for_intercept]
        # sequence_after_intercept = intercepts[index_for_intercept + 1:]
        print('Sequence before intercept: ', sequence_before_intercept)

        intercept_type = find_intercept_type(intercept)

        if (not intercept_type):
            raise Exception('No intercept type found')

        print('Intercept type: ', intercept_type)

        intercept_symmetry_map = {
            'x_intercept': 'x-Axis',
            'y_intercept': 'y-Axis'
        }

        mirror_sequence1 = augment_symmetry(sequence_before_intercept, intercept, intercept_symmetry_map[intercept_type])
        # mirror_sequence2 = augment_symmetry(sequence_after_intercept, intercept_symmetry_map[intercept_type])

        mirrors_from_intercept = {
            'intercept': intercept,
            'mirror1': mirror_sequence1,
            # 'mirror2': mirror_sequence2
        }

        generated_mirrors.append(mirrors_from_intercept)

    print(generated_mirrors)
    for mirror in generated_mirrors:
        plot_points(mirror['mirror1'])
    return generated_mirrors

generate_mirrors_from_intercepts(solution_points)
