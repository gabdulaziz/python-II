import pytest
from problem import Problem
from student import Student
from quiz import Quiz


# ============================================================
#  FIXTURES
# ============================================================

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
def mubarro():
    return Student(
        name="Mubarro",
        group=1,
        problems={i: v for i, v in enumerate(
            [4, 3, 2, 8, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1
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
def maryam():
    return Student(
        name="Maryam",
        group=1,
        problems={i: v for i, v in enumerate(
            [3, 3, 2, 8, 0, 0, 0, 2, 1, 2, 5, 0, 1, 0, 1, 0, 0], 1
        )},
    )


@pytest.fixture
def five_students(timur, shahrom, mubarro, maryam, absent):
    return [timur, shahrom, mubarro, maryam, absent]


@pytest.fixture
def sample_problems():
    texts = [
        "Print output", "Variables", "Conditions", "Loops",
        "Strings", "Lists", "Functions", "Dicts",
        "Sets", "Tuples", "File I/O", "Recursion",
        "Classes", "Error handling", "Algorithms", "Regex", "Final"
    ]
    points = [4, 3, 4, 8, 5, 4, 10, 5, 4, 4, 5, 10, 4, 4, 6, 4, 5]
    return [Problem(number=i + 1, text=texts[i], points=points[i]) for i in range(17)]


@pytest.fixture
def quiz(sample_problems, five_students):
    return Quiz(problems=sample_problems, students=five_students)


# ============================================================
#  PROBLEM — CREATION & DIFFICULTY
# ============================================================

class TestProblemCreation:
    def test_attributes(self):
        p = Problem(number=1, text="Hello", points=4)
        assert p.number == 1
        assert p.text == "Hello"
        assert p.points == 4

    def test_difficulty_easy_1(self):
        assert Problem(number=1, text="t", points=1).difficulty == "easy"

    def test_difficulty_easy_3(self):
        assert Problem(number=1, text="t", points=3).difficulty == "easy"

    def test_difficulty_medium_4(self):
        assert Problem(number=1, text="t", points=4).difficulty == "medium"

    def test_difficulty_medium_6(self):
        assert Problem(number=1, text="t", points=6).difficulty == "medium"

    def test_difficulty_hard_7(self):
        assert Problem(number=1, text="t", points=7).difficulty == "hard"

    def test_difficulty_hard_10(self):
        assert Problem(number=1, text="t", points=10).difficulty == "hard"


# ============================================================
#  PROBLEM — AVG_SCORE
# ============================================================

class TestProblemAvgScore:
    def test_avg_score_problem_1(self, five_students):
        p = Problem(number=1, text="t", points=4)
        # timur=4, shahrom=4, mubarro=4, maryam=3, absent=0 → 15/5=3.0
        assert p.avg_score(five_students) == pytest.approx(3.0)

    def test_avg_score_problem_7(self, five_students):
        p = Problem(number=7, text="t", points=10)
        # timur=10, shahrom=10, mubarro=0, maryam=0, absent=0 → 20/5=4.0
        assert p.avg_score(five_students) == pytest.approx(4.0)

    def test_avg_score_single_student(self, timur):
        p = Problem(number=1, text="t", points=4)
        assert p.avg_score([timur]) == pytest.approx(4.0)

    def test_avg_score_all_absent(self, absent):
        p = Problem(number=5, text="t", points=5)
        assert p.avg_score([absent]) == pytest.approx(0.0)


# ============================================================
#  PROBLEM — TO_DICT
# ============================================================

class TestProblemToDict:
    def test_to_dict_exists(self):
        p = Problem(number=3, text="Conditions", points=4)
        method = None
        for name in ["to_dict", "as_dict", "info"]:
            if hasattr(p, name) and callable(getattr(p, name)):
                method = getattr(p, name)
                break
        assert method is not None, "Problem must have to_dict(), as_dict(), or info() method"

    def test_to_dict_contains_keys(self):
        p = Problem(number=3, text="Conditions", points=4)
        d = None
        for name in ["to_dict", "as_dict", "info"]:
            if hasattr(p, name) and callable(getattr(p, name)):
                d = getattr(p, name)()
                break
        assert isinstance(d, dict)
        assert "number" in d or 3 in d.values()
        assert "points" in d or 4 in d.values()


# ============================================================
#  STUDENT — CREATION
# ============================================================

class TestStudentCreation:
    def test_attributes(self, timur):
        assert timur.name == "Timur"
        assert timur.group == 1
        assert len(timur.problems) == 17

    def test_extra_default(self, timur):
        assert timur.extra_points == 0

    def test_absent_all_zeros(self, absent):
        assert all(v == 0 for v in absent.problems.values())


# ============================================================
#  STUDENT — SCORE
# ============================================================

class TestStudentScore:
    def test_score_timur(self, timur):
        assert timur.get_score() == 89

    def test_score_shahrom(self, shahrom):
        assert shahrom.get_score() == 83

    def test_score_mubarro(self, mubarro):
        assert mubarro.get_score() == 22

    def test_score_absent(self, absent):
        assert absent.get_score() == 0

    def test_score_maryam(self, maryam):
        assert maryam.get_score() == 28

    def test_score_with_extra(self, mubarro):
        mubarro.add_extra(5)
        assert mubarro.get_score() == 27


# ============================================================
#  STUDENT — SOLVED / FAILED
# ============================================================

class TestStudentSolvedFailed:
    def test_solved_all(self, timur):
        assert len(timur.solved_list()) == 17

    def test_solved_none(self, absent):
        assert timur_solved_list_empty(absent)

    def test_solved_partial(self, mubarro):
        solved = mubarro.solved_list()
        assert 1 in solved
        assert 4 in solved
        assert 7 not in solved

    def test_failed_none(self, timur):
        assert len(timur.failed_list()) == 0

    def test_failed_all(self, absent):
        assert len(absent.failed_list()) == 17

    def test_solved_plus_failed(self, maryam):
        assert len(maryam.solved_list()) + len(maryam.failed_list()) == 17


def timur_solved_list_empty(student):
    return student.solved_list() == []


# ============================================================
#  STUDENT — __str__
# ============================================================

class TestStudentStr:
    def test_str_contains_name(self, timur):
        assert "Timur" in str(timur)

    def test_str_contains_score(self, timur):
        assert "89" in str(timur)

    def test_str_returns_string(self, timur):
        assert isinstance(str(timur), str)

    def test_str_absent_student(self, absent):
        s = str(absent)
        assert "Muhammadjon" in s
        assert "0" in s


# ============================================================
#  STUDENT — N, V, K
# ============================================================

class TestStudentNVK:
    def _get_value(self, student, letter):
        for attr in [f"get_{letter}", letter, f"calc_{letter}", f"calculate_{letter}"]:
            if hasattr(student, attr):
                val = getattr(student, attr)
                return val() if callable(val) else val
        return None

    def test_n_exists(self, timur):
        assert self._get_value(timur, "n") is not None, "N method/property not found"

    def test_v_exists(self, timur):
        assert self._get_value(timur, "v") is not None, "V method/property not found"

    def test_k_exists(self, timur):
        assert self._get_value(timur, "k") is not None, "K method/property not found"

    def test_n_is_numeric(self, timur):
        val = self._get_value(timur, "n")
        assert isinstance(val, (int, float))

    def test_v_is_numeric(self, timur):
        val = self._get_value(timur, "v")
        assert isinstance(val, (int, float))

    def test_k_is_numeric(self, timur):
        val = self._get_value(timur, "k")
        assert isinstance(val, (int, float))

    def test_absent_n(self, absent):
        val = self._get_value(absent, "n")
        assert val is not None


# ============================================================
#  QUIZ — CREATION
# ============================================================

class TestQuizCreation:
    def test_quiz_has_problems(self, quiz):
        assert hasattr(quiz, "problems") or hasattr(quiz, "_Quiz__problems")

    def test_quiz_has_students(self, quiz):
        assert hasattr(quiz, "students") or hasattr(quiz, "_Quiz__students")


# ============================================================
#  QUIZ — TOP
# ============================================================

class TestQuizTop:
    def test_top_1(self, quiz):
        top1 = quiz.top(1)
        assert len(top1) == 1
        assert top1[0].name == "Timur"

    def test_top_2(self, quiz):
        top2 = quiz.top(2)
        assert len(top2) == 2
        assert top2[0].name == "Timur"
        assert top2[1].name == "Shahrom"

    def test_top_3_order(self, quiz):
        top3 = quiz.top(3)
        scores = [s.get_score() for s in top3]
        assert scores == sorted(scores, reverse=True)

    def test_top_all(self, quiz):
        top_all = quiz.top(5)
        assert len(top_all) == 5

    def test_top_returns_students(self, quiz):
        top1 = quiz.top(1)
        assert hasattr(top1[0], "name")
        assert hasattr(top1[0], "get_score")


# ============================================================
#  QUIZ — HARDEST / EASIEST PROBLEM
# ============================================================

class TestQuizProblems:
    def test_hardest_returns_problem(self, quiz):
        h = quiz.hardest_problem()
        assert hasattr(h, "number")
        assert hasattr(h, "points")

    def test_easiest_returns_problem(self, quiz):
        e = quiz.easiest_problem()
        assert hasattr(e, "number")
        assert hasattr(e, "points")

    def test_hardest_not_easiest(self, quiz):
        h = quiz.hardest_problem()
        e = quiz.easiest_problem()
        assert h.number != e.number

    def test_easiest_solved_by_more(self, quiz, five_students):
        h = quiz.hardest_problem()
        e = quiz.easiest_problem()
        hard_solved = sum(1 for s in five_students if s.problems.get(h.number, 0) > 0)
        easy_solved = sum(1 for s in five_students if s.problems.get(e.number, 0) > 0)
        assert easy_solved >= hard_solved


# ============================================================
#  QUIZ — AVERAGE SCORE
# ============================================================

class TestQuizAverage:
    def test_average_returns_number(self, quiz):
        avg = quiz.average_score()
        assert isinstance(avg, (int, float))

    def test_average_value(self, quiz):
        # timur=89, shahrom=83, mubarro=22, maryam=28, absent=0
        expected = (89 + 83 + 22 + 28 + 0) / 5  # 44.4
        assert quiz.average_score() == pytest.approx(expected)

    def test_average_positive(self, quiz):
        assert quiz.average_score() > 0


# ============================================================
#  QUIZ — ABOVE_AVERAGE
# ============================================================

class TestQuizAboveAverage:
    def test_above_average_returns_list(self, quiz):
        result = quiz.above_average()
        assert isinstance(result, list)

    def test_above_average_correct_students(self, quiz):
        result = quiz.above_average()
        names = [s.name for s in result]
        avg = quiz.average_score()
        # timur=89 > 44.4 ✅, shahrom=83 > 44.4 ✅, mubarro=22 ❌, maryam=28 ❌, absent=0 ❌
        assert "Timur" in names
        assert "Shahrom" in names
        assert "Muhammadjon" not in names
        assert "Mubarro" not in names

    def test_above_average_count(self, quiz):
        result = quiz.above_average()
        assert len(result) == 2

    def test_above_average_all_above(self, quiz, five_students):
        avg = quiz.average_score()
        for s in quiz.above_average():
            assert s.get_score() > avg


# ============================================================
#  QUIZ — REPORT
# ============================================================

class TestQuizReport:
    def test_report_exists(self, quiz):
        assert hasattr(quiz, "report")
        assert callable(quiz.report)

    def test_report_runs(self, quiz, capsys):
        quiz.report()
        captured = capsys.readouterr()
        assert len(captured.out) > 0

    def test_report_contains_student_names(self, quiz, capsys):
        quiz.report()
        out = capsys.readouterr().out
        assert "Timur" in out
        assert "Shahrom" in out

    def test_report_contains_scores(self, quiz, capsys):
        quiz.report()
        out = capsys.readouterr().out
        assert "89" in out
        assert "83" in out

    def test_report_contains_average(self, quiz, capsys):
        quiz.report()
        out = capsys.readouterr().out
        # average is 44.4 — should appear somewhere
        assert "44" in out or "average" in out.lower()

    def test_report_contains_top(self, quiz, capsys):
        quiz.report()
        out = capsys.readouterr().out.lower()
        assert "top" in out or "rank" in out or "1." in out
