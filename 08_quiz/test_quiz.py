import pytest
from quiz import Student
from quiz import Problem

@pytest.fixture
def timur():
    return Student(
        name="Timur",
        group=1,
        problems={i: v for i, v in enumerate(
            [4, 3, 4, 8, 5, 4, 10, 5, 4, 4, 5, 10, 4, 4, 6, 4, 5], 1
        )},
    )


@pytest.fixture
def shahrom():
    return Student(
        name="Shahrom",
        group=1,
        problems={i: v for i, v in enumerate(
            [4, 3, 4, 8, 5, 4, 10, 5, 3, 3, 4, 10, 4, 4, 6, 4, 2], 1
        )},
    )


@pytest.fixture
def absent():
    return Student(
        name="Muhammadjon",
        group=1,
        problems={i: 0 for i in range(1, 18)},
    )


@pytest.fixture
def partial():
    return Student(
        name="Mubarro",
        group=1,
        problems={i: v for i, v in enumerate(
            [4, 3, 2, 8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1
        )},
    )


@pytest.fixture
def sample_students(timur, shahrom, partial, absent):
    return [timur, shahrom, partial, absent]


@pytest.fixture
def problem_easy():
    return Problem(number=1, text="Print hello world", points=4)


@pytest.fixture
def problem_medium():
    return Problem(number=4, text="Nested loops", points=5)


@pytest.fixture
def problem_hard():
    return Problem(number=7, text="Recursion", points=10)

class TestStudentCreation:
    def test_basic_attributes(self, timur):
        assert timur.name == "Timur"
        assert timur.group == 1

    def test_problems_dict_length(self, timur):
        assert len(timur.problems) == 17

    def test_problems_dict_values(self, timur):
        assert timur.problems[1] == 4
        assert timur.problems[7] == 10
        assert timur.problems[17] == 5

    def test_extra_points_default(self, timur):
        assert timur.extra_points == 0

    def test_absent_student_all_zeros(self, absent):
        assert all(v == 0 for v in absent.problems.values())

    def test_absent_student_17_problems(self, absent):
        assert len(absent.problems) == 17

class TestStudentScore:
    def test_score_timur(self, timur):
        assert timur.get_score() == 89

    def test_score_shahrom(self, shahrom):
        assert shahrom.get_score() == 83

    def test_score_absent(self, absent):
        assert absent.get_score() == 0

    def test_score_partial(self, partial):
        assert partial.get_score() == 22

    def test_score_with_extra(self, partial):
        partial.add_extra(5)
        assert partial.get_score() == 27

    def test_score_with_multiple_extra(self, absent):
        absent.add_extra(3)
        absent.add_extra(2)
        assert absent.get_score() == 5

class TestStudentExtra:
    def test_add_extra_once(self, timur):
        timur.add_extra(5)
        assert timur.extra_points == 5

    def test_add_extra_accumulates(self, timur):
        timur.add_extra(3)
        timur.add_extra(2)
        assert timur.extra_points == 5

    def test_add_extra_zero(self, timur):
        timur.add_extra(0)
        assert timur.extra_points == 0

class TestStudentSolvedFailed:
    def test_solved_list_timur(self, timur):
        solved = timur.solved_list()
        assert len(solved) == 17
        assert 1 in solved
        assert 7 in solved

    def test_solved_list_partial(self, partial):
        solved = partial.solved_list()
        assert len(solved) == 5
        assert 1 in solved
        assert 5 in solved
        assert 6 not in solved

    def test_solved_list_absent(self, absent):
        assert absent.solved_list() == []

    def test_failed_list_timur(self, timur):
        assert timur.failed_list() == []

    def test_failed_list_partial(self, partial):
        failed = partial.failed_list()
        assert len(failed) == 12
        assert 6 in failed
        assert 17 in failed

    def test_failed_list_absent(self, absent):
        assert len(absent.failed_list()) == 17

    def test_solved_plus_failed_equals_17(self, shahrom):
        assert len(shahrom.solved_list()) + len(shahrom.failed_list()) == 17


class TestStudentDisplay:
    def test_display_exists(self, timur):
        assert hasattr(timur, "display")
        assert callable(timur.display)

    def test_display_runs(self, timur, capsys):
        timur.display()
        captured = capsys.readouterr()
        assert "Timur" in captured.out

    def test_display_shows_score(self, timur, capsys):
        timur.display()
        captured = capsys.readouterr()
        assert "89" in captured.out



class TestStudentNVK:
    def test_n_method_exists(self, timur):
        # N should be related to number of solved problems or similar metric
        # Student must have a method for N
        result = None
        for method_name in ["get_n", "n", "calc_n", "calculate_n"]:
            if hasattr(timur, method_name) and callable(getattr(timur, method_name)):
                result = getattr(timur, method_name)()
                break
        if result is None and hasattr(timur, "n") and not callable(getattr(timur, "n")):
            result = timur.n
        assert result is not None, "Student must have a method or property for N"

    def test_v_method_exists(self, timur):
        result = None
        for method_name in ["get_v", "v", "calc_v", "calculate_v"]:
            if hasattr(timur, method_name) and callable(getattr(timur, method_name)):
                result = getattr(timur, method_name)()
                break
        if result is None and hasattr(timur, "v") and not callable(getattr(timur, "v")):
            result = timur.v
        assert result is not None, "Student must have a method or property for V"

    def test_k_method_exists(self, timur):
        result = None
        for method_name in ["get_k", "k", "calc_k", "calculate_k"]:
            if hasattr(timur, method_name) and callable(getattr(timur, method_name)):
                result = getattr(timur, method_name)()
                break
        if result is None and hasattr(timur, "k") and not callable(getattr(timur, "k")):
            result = timur.k
        assert result is not None, "Student must have a method or property for K"


class TestProblemCreation:
    def test_basic_attributes(self, problem_easy):
        assert problem_easy.number == 1
        assert problem_easy.text == "Print hello world"
        assert problem_easy.points == 4

    def test_difficulty_easy(self):
        for pts in [1, 2, 3]:
            p = Problem(number=1, text="test", points=pts)
            assert p.difficulty == "easy", f"points={pts} should be easy"

    def test_difficulty_medium(self):
        for pts in [4, 5, 6]:
            p = Problem(number=1, text="test", points=pts)
            assert p.difficulty == "medium", f"points={pts} should be medium"

    def test_difficulty_hard(self):
        for pts in [7, 8, 10]:
            p = Problem(number=1, text="test", points=pts)
            assert p.difficulty == "hard", f"points={pts} should be hard"



class TestProblemAvgScore:
    def test_avg_score_problem_1(self, sample_students):
        p = Problem(number=1, text="test", points=4)
        avg = p.avg_score(sample_students)
        # timur=4, shahrom=4, partial=4, absent=0 → avg=3.0
        assert avg == pytest.approx(3.0)

    def test_avg_score_problem_7(self, sample_students):
        p = Problem(number=7, text="test", points=10)
        avg = p.avg_score(sample_students)
        # timur=10, shahrom=10, partial=0, absent=0 → avg=5.0
        assert avg == pytest.approx(5.0)

    def test_avg_score_all_zeros(self, sample_students):
        p = Problem(number=17, text="test", points=5)
        # timur=5, shahrom=2, partial=0, absent=0 → avg=1.75
        avg = p.avg_score(sample_students)
        assert avg == pytest.approx(1.75)

    def test_avg_score_single_student(self, timur):
        p = Problem(number=1, text="test", points=4)
        avg = p.avg_score([timur])
        assert avg == pytest.approx(4.0)

    def test_avg_score_all_absent(self, absent):
        p = Problem(number=1, text="test", points=4)
        avg = p.avg_score([absent])
        assert avg == pytest.approx(0.0)


class TestProblemDisplay:
    def test_display_exists(self, problem_easy):
        assert hasattr(problem_easy, "display")
        assert callable(problem_easy.display)
