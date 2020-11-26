import pytest
import ast
import inspect
from exercises.tutorial07 import index_bisect
from exercises.tutorial07 import recursive_polynomial
from exercises.tutorial07 import alternating_sequence, neg_pos, pos_neg
from exercises.tutorial07 import Lucas
import random
import bisect


class TestExercise3_4_1_1:

    def test_no_for(self):
        if any(isinstance(node, ast.For) for node in ast.walk(ast.parse(inspect.getsource(recursive_polynomial)))):
            pytest.fail("The method 'recursive_polynomial' should not contain a for loop!")

    def test_no_while(self):
        if any(isinstance(node, ast.While) for node in ast.walk(ast.parse(inspect.getsource(recursive_polynomial)))):
            pytest.fail("The method 'recursive_polynomial' should not contain a while loop!")

    @pytest.mark.parametrize("a_list, x, expected",
                             [([7], 4, 7),
                              ([1, 4], 4, 8),
                              ([], 4, 0),
                              ([1, 2, 1], 4, 25),
                              ([1, 2, -3, 2, -1], 2, 23)])
    def test_polynomial(self, a_list, x, expected):
        result = recursive_polynomial(a_list, x)
        if expected != result:
            pytest.fail(
                "The method 'recursive_polynomial' fails for\n list {}\n value {}.\n Answer is {}.\n Should be {}.".format(
                    a_list, x, result, expected))


# No need to change these tests.

class TestExercise3_4_2_1:

    def test_no_for(self):
        if (any(isinstance(node, ast.For) for node in ast.walk(ast.parse(inspect.getsource(index_bisect))))):
            pytest.fail("The method 'index_bisect' should not contain a for loop!")

    def test_no_while(self):
        if (any(isinstance(node, ast.While) for node in ast.walk(ast.parse(inspect.getsource(index_bisect))))):
            pytest.fail("The method 'index_bisect' should not contain a while loop!")

    def test_insert(self):
        for i in range(100):
            sample_size = random.randrange(3, 33)
            some_randoms = random.sample(range(100), sample_size)
            some_randoms.sort()
            some_value = random.randrange(-10, 110)
            expected = some_randoms.copy()
            result = some_randoms.copy()
            bisect.insort(expected, some_value)
            insertion_index = index_bisect(result, some_value)
            result.insert(insertion_index, some_value)
            if expected != result:
                pytest.fail(
                    "The method 'insort_bisect' fails for\n value {}\n list {}.\n Answer is {}.\n Should be {}.".format(
                        some_value, some_randoms, result, expected))


class TestExercise3_4_3_2:

    def test_no_for(self):
        if (any(isinstance(node, ast.For) for node in ast.walk(ast.parse(inspect.getsource(neg_pos))))):
            pytest.fail("The method 'neg_pos' should not contain a for loop!")
        if (any(isinstance(node, ast.For) for node in ast.walk(ast.parse(inspect.getsource(pos_neg))))):
            pytest.fail("The method 'pos_neg' should not contain a for loop!")

    def test_no_while(self):
        if (any(isinstance(node, ast.While) for node in ast.walk(ast.parse(inspect.getsource(neg_pos))))):
            pytest.fail("The method 'neg_pos' should not contain a while loop!")
        if (any(isinstance(node, ast.While) for node in ast.walk(ast.parse(inspect.getsource(pos_neg))))):
            pytest.fail("The method 'pos_neg' should not contain a while loop!")

    def test_odd_even_alternation(self):
        for a_list, expected in [([], True),
                                 ([1], True),
                                 ([-4], True),
                                 ([-1, 2, -1], True),
                                 ([-1, 2, -3, 2, -1], True),
                                 ([12, -1, 2, -1], True),
                                 ([12, -1, -2, 1], False),
                                 ([-7, 12, -9, 2, -1, -3], False)]:
            result = alternating_sequence(a_list)

            if expected != result:
                pytest.fail(
                    "The method 'alternating_sequence' fails for\n list {}.\n Answer is {}, should be {}.".format(
                        a_list, result, expected))


class TestExercise3_4_4_1:

    def test_lucas(self):
        for n, f_n, steps_n in [(5, 11, 4),
                                (10, 123, 9),
                                (20, 15127, 19)]:
            l = Lucas(2, 1)
            result = l.solve_memoized(n)
            steps = l.get_counter()

            if result != f_n or steps != steps_n:
                pytest.fail(
                    "The method 'solve_memoized' fails for\n input n {}.\n Answer is {}, steps taken {}\n Should be {} with {} steps.".format(
                        n, result, steps, f_n, steps_n))
                return None

        print("Method 'solve_memoized' seems to work")


