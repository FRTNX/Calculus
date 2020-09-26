import mock
import pytest
from pytest_mock import mocker
import psycopg2.errors
from unittest.mock import Mock
from main import *


def test_find_solution_points_from_graph_equation():
    graph_equation = 'y == (x ** 3) - x'
    expected_solution_points = [[-4, -60], [-3, -24], [-2, -6], [-1, 0], [0, 0], [1, 0], [2, 6], [3, 24], [4, 60]]
    solution_points = find_solution_points_from_graph_equation(graph_equation, -100, 100)
    assert solution_points == expected_solution_points


def test_find_solution_points_from_point_slope():
    expected_equation = 'y == (3 * x) - 5' # simplified

    solution_points_from_point_slope = find_solution_points_from_point_slope([1, -2], 3, -10, 10)
    solution_points_from_graph_equation = find_solution_points_from_graph_equation(expected_equation, -10, 10)

    assert solution_points_from_point_slope == solution_points_from_graph_equation


def test_find_solution_points_from_slope_intercept():
    assert find_solution_points_from_slope_intercept([0, 1], 2) == find_solution_points_from_graph_equation('y == (2 * x) + 1')
    assert find_solution_points_from_slope_intercept([0, 2], 0) == find_solution_points_from_graph_equation('y == 2')

    slope = -0.3333333333333333
    expected_equation = f'y == ({slope} * x) + 2'
    assert find_solution_points_from_slope_intercept([0, 2], slope) == find_solution_points_from_graph_equation(expected_equation)


def test_find_intercepts():
    solution_points = [[-4, -60], [-3, -24], [-2, -6], [-1, 0], [0, 0], [1, 0], [2, 6], [3, 24], [4, 60]]
    expected_intercepts = [[-1, 0], [0, 0], [1, 0]]
    intercepts = find_intercepts(solution_points)
    assert intercepts == expected_intercepts


def test_find_intercept_type():
    assert find_intercept_type([0, 0]) == 'origin'
    assert find_intercept_type([4, 0]) == 'x_intercept'
    assert find_intercept_type([0, 16]) == 'y_intercept'


def test_check_for_symmetry():
    solution_points = [[-4, -60], [-3, -24], [-2, -6], [-1, 0], [0, 0], [1, 0], [2, 6], [3, 24], [4, 60]]
    assert check_for_symmetry(solution_points) == {
        'origin_symmetry': True,
        'x_axis_symmetry': False,
        'y_axis_symmetry': False
    }

    # Resolve for this type of x-symmetry, expand to others
    # solution_points = [[1, 0], [2, -1], [2, 1], [5, -2], [5, 2], [10, -3], [10, 3], [17, -4],
    #     [17, 4], [26, -5], [26, 5], [37, -6], [37, 6], [50, -7], [50, 7], [65, -8], [65, 8],
    #     [82, -9], [82, 9]]
    # assert check_for_symmetry(solution_points) == {
    #     'origin_symmetry': False,
    #     'x_axis_symmetry': True,
    #     'y_axis_symmetry': False
    # }


    solution_points = [
        [-10, -96], [-9, -77], [-8, -60], [-7, -45], [-6, -32], [-5, -21], [-4, -12],
        [-3, -5], [-2, 0], [-1, 3], [0, 4], [1, 3], [2, 0], [3, -5], [4, -12],
        [5, -21], [6, -32], [7, -45], [8, -60], [9, -77], [10, -96]
    ]
    assert check_for_symmetry(solution_points) == {
        'origin_symmetry': False,
        'x_axis_symmetry': False,
        'y_axis_symmetry': True
    }


def test_generate_mirrors_from_intercepts():
    solution_points = [[-4, -60], [-3, -24], [-2, -6], [-1, 0], [0, 0], [1, 0], [2, 6], [3, 24], [4, 60]]
    expected_mirrors = [
        {
            'intercept': [-1, 0],
            'mirror1': [[-4, -60], [-3, -24], [-2, -6], [-1, 0], [2, -6], [3, -24], [4, -60]]
        },
        {
            'intercept': [0, 0],
            'mirror1': ['origin_symmetry_mirror_not_supported_yet']
        },
        {
            'intercept': [1, 0],
            'mirror1': [[-4, -60], [-3, -24], [-2, -6], [-1, 0], [0, 0], [1, 0], [0, 0], [1, 0], [2, -6], [3, -24], [4, -60]]
        }
    ]

    assert generate_mirrors_from_intercepts(solution_points) == expected_mirrors


def test_find_intersections():
    graph_equations = ['x - y == 1', 'x ** 2 - y == 3']
    expected_intersections = [[-1, -2], [2, 1]]

    # Path 1, passing in any number graph equations
    intersections = find_intersections(graph_equations)
    assert len(intersections) == 2

    assert [-1, -2] in intersections
    assert [2, 1] in intersections

    solution_points_array = [
        [[-3, -4], [-2, -3], [-1, -2], [0, -1], [1, 0], [2, 1], [3, 2], [4, 3]],
        [[-5, 22], [-4, 13], [-3, 6], [-2, 1], [-1, -2], [0, -3], [1, -2], [2, 1], [3, 6], [4, 13], [5, 22]]
    ]

    # Path 2, passing in solution points of any number of equations
    intersections = find_intersections([], solution_points_array)
    assert len(intersections) == 2

    assert [-1, -2] in intersections
    assert [2, 1] in intersections


def test_calculate_slope():
    assert calculate_slope([-2, 0], [3, 1]) == 0.2 # rise /
    assert calculate_slope([-1, 2], [2, 2]) == 0.0 # horizontal --
    assert calculate_slope([0, 4], [1, -1]) == -5  # fall \
    assert calculate_slope([3, 4], [3, 1]) == None # vertical |


def test_is_parallel():
    assert is_parallel('(2 * x) - (3 * y) == 5', '(2 * x) - (3 * y) == 7') == True
    assert is_parallel('(2 * x) - (3 * y) == 7', '(2 * x) - (3 * y) == 5') == True
    # todo: more tests


def test_is_perpendicular():
    assert is_perpendicular('(2 * x) - (3 * y) == 5', '(3 * x) + (2 * y) == 4') == True
    assert is_perpendicular('(3 * x) + (2 * y) == 4', '(2 * x) - (3 * y) == 5') == True
    # todo: more tests
