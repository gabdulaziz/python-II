import math
import sys


# ============================================================
#  IMPORTS
# ============================================================

def safe_import(module_path, class_name):
    try:
        module = __import__(module_path, fromlist=[class_name])
        return getattr(module, class_name)
    except (ImportError, AttributeError):
        return None


Temperature = safe_import("temperature.temperature", "Temperature")
Counter = safe_import("counter.counter", "Counter")
Fraction = safe_import("fraction.fraction", "Fraction")
Inventory = safe_import("inventory.inventory", "Inventory")
Leaderboard = safe_import("leaderboard.leaderboard", "Leaderboard")
Matrix2x2 = safe_import("matrix2x2.matrix2x2", "Matrix2x2")
Playlist = safe_import("playlist.playlist", "Playlist")
RGBColor = safe_import("rgb_color.rgb_color", "RGBColor")
Vector = safe_import("vector.vector", "Vector")
WordBox = safe_import("word_box.word_box", "WordBox")


class TestRunner:
    def __init__(self):
        self.results = {}

    def run_tests(self, name, cls, tests):
        if cls is None:
            self.results[name] = {"passed": 0, "total": len(tests), "details": [], "skipped": True}
            return

        passed = 0
        details = []
        for test_name, fn in tests:
            try:
                fn()
                passed += 1
                details.append(("✅", test_name))
            except Exception as e:
                details.append(("❌", f"{test_name}: {e}"))

        self.results[name] = {"passed": passed, "total": len(tests), "details": details, "skipped": False}

    def print_report(self):
        print("\n" + "=" * 60)
        print("  DUNDER METHODS — TEST RESULTS")
        print("=" * 60)

        total_score = 0
        max_score = 100

        for name, r in self.results.items():
            if r["skipped"]:
                score = 0
                bar = "░" * 20
                print(f"\n⬜ {name} — NOT FOUND (0/{r['total']} tests)")
                print(f"   {bar} 0.0 / 10.0 pts")
                continue

            pct = r["passed"] / r["total"] if r["total"] > 0 else 0
            score = round(pct * 10, 1)
            total_score += score

            filled = int(pct * 20)
            bar = "█" * filled + "░" * (20 - filled)

            if pct == 1:
                icon = "🏆"
            elif pct >= 0.7:
                icon = "🟡"
            else:
                icon = "🔴"

            print(f"\n{icon} {name} — {r['passed']}/{r['total']} tests passed")
            print(f"   {bar} {score} / 10.0 pts")

            for status, detail in r["details"]:
                if status == "❌":
                    print(f"   {status} {detail}")

        print("\n" + "=" * 60)
        pct_total = round(total_score / max_score * 100, 1)
        filled = int(pct_total / 100 * 30)
        bar = "█" * filled + "░" * (30 - filled)
        print(f"  TOTAL: {total_score} / {max_score} pts ({pct_total}%)")
        print(f"  {bar}")

        if pct_total == 100:
            print("\n  🎉 PERFECT SCORE! You're a dunder master!")
        elif pct_total >= 80:
            print("\n  💪 Great job! Almost there!")
        elif pct_total >= 50:
            print("\n  📚 Good progress. Keep practicing!")
        else:
            print("\n  🌱 Keep going — every expert was once a beginner!")

        print("=" * 60)



class AssertionError(Exception):
    pass

def assertEqual(a, b):
    if a != b:
        raise AssertionError(f"Expected {b!r}, got {a!r}")

def assertTrue(val):
    if not val:
        raise AssertionError(f"Expected True, got {val!r}")

def assertFalse(val):
    if val:
        raise AssertionError(f"Expected False, got {val!r}")


runner = TestRunner()


temperature_tests = [
    ("str basic", lambda: (
        assertEqual(str(Temperature(25)), "25°C")
    )),
    ("str zero", lambda: (
        assertEqual(str(Temperature(0)), "0°C")
    )),
    ("str negative", lambda: (
        assertEqual(str(Temperature(-10)), "-10°C")
    )),
    ("eq same", lambda: (
        assertTrue(Temperature(25) == Temperature(25))
    )),
    ("eq different", lambda: (
        assertFalse(Temperature(25) == Temperature(30))
    )),
    ("lt true", lambda: (
        assertTrue(Temperature(10) < Temperature(20))
    )),
    ("lt false", lambda: (
        assertFalse(Temperature(30) < Temperature(10))
    )),
    ("lt equal", lambda: (
        assertFalse(Temperature(10) < Temperature(10))
    )),
    ("add", lambda: (
        assertEqual(str(Temperature(25) + Temperature(30)), "55°C")
    )),
    ("add negative", lambda: (
        assertEqual(str(Temperature(10) + Temperature(-3)), "7°C")
    )),
    ("add does not mutate", lambda: (
        _check_no_mutate_temp()
    )),
    ("sorted", lambda: (
        assertEqual(
            [str(t) for t in sorted([Temperature(30), Temperature(10), Temperature(20)])],
            ["10°C", "20°C", "30°C"]
        )
    )),
]


def _check_no_mutate_temp():
    a, b = Temperature(10), Temperature(20)
    _ = a + b
    assertEqual(str(a), "10°C")
    assertEqual(str(b), "20°C")


runner.run_tests("Temperature", Temperature, temperature_tests)


wordbox_tests = [
    ("len empty", lambda: (
        assertEqual(len(WordBox()), 0)
    )),
    ("len after add", lambda: (
        _check_wb_len()
    )),
    ("contains lowercase", lambda: (
        _check_wb_contains("hello", True)
    )),
    ("contains uppercase", lambda: (
        _check_wb_contains("HELLO", True)
    )),
    ("contains mixed case", lambda: (
        _check_wb_contains("HeLLo", True)
    )),
    ("contains missing", lambda: (
        _check_wb_contains("java", False)
    )),
    ("str format", lambda: (
        _check_wb_str()
    )),
    ("stores lowercase", lambda: (
        _check_wb_stores_lower()
    )),
    ("add multiple same", lambda: (
        _check_wb_duplicates()
    )),
    ("contains empty box", lambda: (
        assertFalse("hello" in WordBox())
    )),
]


def _make_wb():
    b = WordBox()
    b.add("Hello")
    b.add("World")
    b.add("Python")
    return b

def _check_wb_len():
    assertEqual(len(_make_wb()), 3)

def _check_wb_contains(word, expected):
    b = _make_wb()
    assertEqual(word in b, expected)

def _check_wb_str():
    assertEqual(str(_make_wb()), "WordBox(3 words: hello, world, python)")

def _check_wb_stores_lower():
    b = WordBox()
    b.add("UPPER")
    assertTrue("upper" in b)

def _check_wb_duplicates():
    b = WordBox()
    b.add("test")
    b.add("test")
    assertEqual(len(b), 2)


runner.run_tests("WordBox", WordBox, wordbox_tests)


counter_tests = [
    ("str default", lambda: (
        assertEqual(str(Counter()), "Counter(0)")
    )),
    ("str with value", lambda: (
        assertEqual(str(Counter(42)), "Counter(42)")
    )),
    ("increment", lambda: (
        _check_counter_inc()
    )),
    ("eq same", lambda: (
        assertTrue(Counter(5) == Counter(5))
    )),
    ("eq different", lambda: (
        assertFalse(Counter(5) == Counter(3))
    )),
    ("add", lambda: (
        assertEqual(str(Counter(3) + Counter(7)), "Counter(10)")
    )),
    ("add does not mutate", lambda: (
        _check_counter_no_mutate()
    )),
    ("bool true", lambda: (
        assertTrue(bool(Counter(1)))
    )),
    ("bool false", lambda: (
        assertFalse(bool(Counter(0)))
    )),
    ("bool after increment", lambda: (
        _check_counter_bool_inc()
    )),
]


def _check_counter_inc():
    c = Counter()
    c.increment()
    c.increment()
    c.increment()
    assertEqual(str(c), "Counter(3)")

def _check_counter_no_mutate():
    a, b = Counter(3), Counter(7)
    _ = a + b
    assertEqual(str(a), "Counter(3)")

def _check_counter_bool_inc():
    c = Counter()
    assertFalse(bool(c))
    c.increment()
    assertTrue(bool(c))


runner.run_tests("Counter", Counter, counter_tests)



fraction_tests = [
    ("str simple", lambda: (
        assertEqual(str(Fraction(1, 2)), "1/2")
    )),
    ("str simplifies", lambda: (
        assertEqual(str(Fraction(2, 4)), "1/2")
    )),
    ("str whole-like", lambda: (
        assertEqual(str(Fraction(6, 3)), "2/1")
    )),
    ("eq same", lambda: (
        assertTrue(Fraction(1, 2) == Fraction(1, 2))
    )),
    ("eq equivalent", lambda: (
        assertTrue(Fraction(1, 2) == Fraction(2, 4))
    )),
    ("eq different", lambda: (
        assertFalse(Fraction(1, 2) == Fraction(1, 3))
    )),
    ("lt true", lambda: (
        assertTrue(Fraction(1, 3) < Fraction(1, 2))
    )),
    ("lt false", lambda: (
        assertFalse(Fraction(1, 2) < Fraction(1, 3))
    )),
    ("add basic", lambda: (
        assertEqual(str(Fraction(1, 2) + Fraction(1, 3)), "5/6")
    )),
    ("add simplifies", lambda: (
        assertEqual(str(Fraction(1, 4) + Fraction(1, 4)), "1/2")
    )),
    ("add same denom", lambda: (
        assertEqual(str(Fraction(1, 5) + Fraction(2, 5)), "3/5")
    )),
    ("repr in list", lambda: (
        _check_fraction_repr()
    )),
]


def _check_fraction_repr():
    f = Fraction(3, 4)
    r = repr(f)
    assertTrue("3" in r and "4" in r)


runner.run_tests("Fraction", Fraction, fraction_tests)


leaderboard_tests = [
    ("len empty", lambda: (
        assertEqual(len(Leaderboard()), 0)
    )),
    ("len after add", lambda: (
        assertEqual(len(_make_lb()), 3)
    )),
    ("getitem rank 1", lambda: (
        assertEqual(_make_lb()[0], {"name": "Bob", "score": 500})
    )),
    ("getitem rank 2", lambda: (
        assertEqual(_make_lb()[1], {"name": "Alice", "score": 300})
    )),
    ("getitem rank 3", lambda: (
        assertEqual(_make_lb()[2], {"name": "Charlie", "score": 150})
    )),
    ("getitem negative index", lambda: (
        assertEqual(_make_lb()[-1], {"name": "Charlie", "score": 150})
    )),
    ("contains found", lambda: (
        assertTrue("Alice" in _make_lb())
    )),
    ("contains not found", lambda: (
        assertFalse("Dave" in _make_lb())
    )),
    ("str has names", lambda: (
        _check_lb_str_content()
    )),
    ("sorted after late add", lambda: (
        _check_lb_resort()
    )),
]


def _make_lb():
    lb = Leaderboard()
    lb.add("Alice", 300)
    lb.add("Bob", 500)
    lb.add("Charlie", 150)
    return lb

def _check_lb_str_content():
    s = str(_make_lb())
    assertTrue("Bob" in s and "500" in s and "Alice" in s)

def _check_lb_resort():
    lb = _make_lb()
    lb.add("Dave", 999)
    assertEqual(lb[0], {"name": "Dave", "score": 999})


runner.run_tests("Leaderboard", Leaderboard, leaderboard_tests)



rgb_tests = [
    ("str", lambda: (
        assertEqual(str(RGBColor(255, 0, 0)), "rgb(255, 0, 0)")
    )),
    ("str black", lambda: (
        assertEqual(str(RGBColor(0, 0, 0)), "rgb(0, 0, 0)")
    )),
    ("repr", lambda: (
        assertEqual(repr(RGBColor(0, 0, 255)), "RGBColor(0, 0, 255)")
    )),
    ("eq same", lambda: (
        assertTrue(RGBColor(255, 0, 0) == RGBColor(255, 0, 0))
    )),
    ("eq different", lambda: (
        assertFalse(RGBColor(255, 0, 0) == RGBColor(0, 0, 255))
    )),
    ("add mix", lambda: (
        assertEqual(str(RGBColor(255, 0, 0) + RGBColor(0, 0, 255)), "rgb(127, 0, 127)")
    )),
    ("add white black", lambda: (
        assertEqual(str(RGBColor(255, 255, 255) + RGBColor(0, 0, 0)), "rgb(127, 127, 127)")
    )),
    ("add same", lambda: (
        assertEqual(str(RGBColor(100, 100, 100) + RGBColor(100, 100, 100)), "rgb(100, 100, 100)")
    )),
    ("contains red in red", lambda: (
        assertTrue("red" in RGBColor(255, 0, 0))
    )),
    ("contains green not in red", lambda: (
        assertFalse("green" in RGBColor(255, 0, 0))
    )),
    ("contains blue in blue", lambda: (
        assertTrue("blue" in RGBColor(0, 0, 255))
    )),
    ("contains all in white", lambda: (
        _check_rgb_white_contains()
    )),
]


def _check_rgb_white_contains():
    w = RGBColor(255, 255, 255)
    assertTrue("red" in w)
    assertTrue("green" in w)
    assertTrue("blue" in w)


runner.run_tests("RGBColor", RGBColor, rgb_tests)



matrix_tests = [
    ("str", lambda: (
        assertEqual(str(Matrix2x2(1, 2, 3, 4)), "|1 2|\n|3 4|")
    )),
    ("str large nums", lambda: (
        assertEqual(str(Matrix2x2(10, 20, 30, 40)), "|10 20|\n|30 40|")
    )),
    ("eq same", lambda: (
        assertTrue(Matrix2x2(1, 2, 3, 4) == Matrix2x2(1, 2, 3, 4))
    )),
    ("eq different", lambda: (
        assertFalse(Matrix2x2(1, 2, 3, 4) == Matrix2x2(5, 6, 7, 8))
    )),
    ("getitem row 0", lambda: (
        assertEqual(Matrix2x2(1, 2, 3, 4)[0], [1, 2])
    )),
    ("getitem row 1", lambda: (
        assertEqual(Matrix2x2(1, 2, 3, 4)[1], [3, 4])
    )),
    ("getitem cell", lambda: (
        assertEqual(Matrix2x2(1, 2, 3, 4)[0][1], 2)
    )),
    ("getitem cell row1", lambda: (
        assertEqual(Matrix2x2(1, 2, 3, 4)[1][0], 3)
    )),
    ("add", lambda: (
        assertEqual(str(Matrix2x2(1, 2, 3, 4) + Matrix2x2(5, 6, 7, 8)), "|6 8|\n|10 12|")
    )),
    ("add does not mutate", lambda: (
        _check_matrix_no_mutate()
    )),
    ("add zeros", lambda: (
        assertEqual(str(Matrix2x2(1, 2, 3, 4) + Matrix2x2(0, 0, 0, 0)), "|1 2|\n|3 4|")
    )),
    ("add negative", lambda: (
        assertEqual(str(Matrix2x2(5, 5, 5, 5) + Matrix2x2(-1, -2, -3, -4)), "|4 3|\n|2 1|")
    )),
]


def _check_matrix_no_mutate():
    a = Matrix2x2(1, 2, 3, 4)
    b = Matrix2x2(5, 6, 7, 8)
    _ = a + b
    assertEqual(str(a), "|1 2|\n|3 4|")


runner.run_tests("Matrix2x2", Matrix2x2, matrix_tests)



inventory_tests = [
    ("len empty", lambda: (
        assertEqual(len(Inventory()), 0)
    )),
    ("len after add", lambda: (
        _check_inv_len()
    )),
    ("contains found", lambda: (
        _check_inv_contains("Sword", True)
    )),
    ("contains not found", lambda: (
        _check_inv_contains("Arrow", False)
    )),
    ("getitem exists", lambda: (
        _check_inv_getitem("Potion", 3)
    )),
    ("getitem missing returns 0", lambda: (
        _check_inv_getitem("Arrow", 0)
    )),
    ("add stacks quantity", lambda: (
        _check_inv_add_stack()
    )),
    ("remove partial", lambda: (
        _check_inv_remove_partial()
    )),
    ("remove completely", lambda: (
        _check_inv_remove_full()
    )),
    ("add two inventories", lambda: (
        _check_inv_merge()
    )),
    ("add does not mutate", lambda: (
        _check_inv_no_mutate()
    )),
    ("eq same", lambda: (
        _check_inv_eq()
    )),
    ("eq different", lambda: (
        _check_inv_neq()
    )),
    ("str has items", lambda: (
        _check_inv_str()
    )),
]


def _make_inv():
    i = Inventory()
    i.add("Sword")
    i.add("Potion", 3)
    i.add("Shield")
    return i

def _check_inv_len():
    assertEqual(len(_make_inv()), 5)

def _check_inv_contains(item, expected):
    assertEqual(item in _make_inv(), expected)

def _check_inv_getitem(item, expected):
    assertEqual(_make_inv()[item], expected)

def _check_inv_add_stack():
    i = Inventory()
    i.add("Potion", 2)
    i.add("Potion", 3)
    assertEqual(i["Potion"], 5)

def _check_inv_remove_partial():
    i = _make_inv()
    i.remove("Potion", 2)
    assertEqual(i["Potion"], 1)

def _check_inv_remove_full():
    i = _make_inv()
    i.remove("Potion", 3)
    assertFalse("Potion" in i)

def _check_inv_merge():
    i1 = _make_inv()
    i2 = Inventory()
    i2.add("Potion", 2)
    i2.add("Arrow", 10)
    i3 = i1 + i2
    assertEqual(i3["Potion"], 5)
    assertEqual(i3["Arrow"], 10)
    assertEqual(i3["Sword"], 1)

def _check_inv_no_mutate():
    i1 = _make_inv()
    i2 = Inventory()
    i2.add("Arrow", 5)
    _ = i1 + i2
    assertEqual(i1["Potion"], 3)
    assertFalse("Arrow" in i1)

def _check_inv_eq():
    a = Inventory()
    a.add("Sword", 2)
    b = Inventory()
    b.add("Sword", 2)
    assertTrue(a == b)

def _check_inv_neq():
    a = Inventory()
    a.add("Sword", 2)
    b = Inventory()
    b.add("Sword", 3)
    assertFalse(a == b)

def _check_inv_str():
    s = str(_make_inv())
    assertTrue("Sword" in s and "Potion" in s)


runner.run_tests("Inventory", Inventory, inventory_tests)


playlist_tests = [
    ("len empty", lambda: (
        assertEqual(len(Playlist("Empty")), 0)
    )),
    ("len after add", lambda: (
        assertEqual(len(_make_pl()), 2)
    )),
    ("contains found", lambda: (
        assertTrue("Bohemian Rhapsody" in _make_pl())
    )),
    ("contains not found", lambda: (
        assertFalse("Hey Jude" in _make_pl())
    )),
    ("getitem 0", lambda: (
        assertEqual(_make_pl()[0], {"title": "Bohemian Rhapsody", "duration": 354})
    )),
    ("getitem 1", lambda: (
        assertEqual(_make_pl()[1], {"title": "Stairway to Heaven", "duration": 482})
    )),
    ("getitem negative", lambda: (
        assertEqual(_make_pl()[-1], {"title": "Stairway to Heaven", "duration": 482})
    )),
    ("add merges", lambda: (
        _check_pl_merge_len()
    )),
    ("add name", lambda: (
        _check_pl_merge_name()
    )),
    ("add does not mutate", lambda: (
        _check_pl_no_mutate()
    )),
    ("eq same", lambda: (
        _check_pl_eq()
    )),
    ("eq different order", lambda: (
        _check_pl_neq_order()
    )),
    ("str total duration", lambda: (
        _check_pl_str_duration()
    )),
    ("str song durations", lambda: (
        _check_pl_str_songs()
    )),
]


def _make_pl():
    p = Playlist("Rock")
    p.add("Bohemian Rhapsody", 354)
    p.add("Stairway to Heaven", 482)
    return p

def _check_pl_merge_len():
    pop = Playlist("Pop")
    pop.add("Blinding Lights", 200)
    merged = _make_pl() + pop
    assertEqual(len(merged), 3)

def _check_pl_merge_name():
    pop = Playlist("Pop")
    pop.add("Blinding Lights", 200)
    merged = _make_pl() + pop
    assertEqual(merged.name, "Rock + Pop")

def _check_pl_no_mutate():
    rock = _make_pl()
    pop = Playlist("Pop")
    pop.add("Blinding Lights", 200)
    _ = rock + pop
    assertEqual(len(rock), 2)

def _check_pl_eq():
    a = _make_pl()
    b = _make_pl()
    assertTrue(a == b)

def _check_pl_neq_order():
    a = Playlist("A")
    a.add("X", 100)
    a.add("Y", 200)
    b = Playlist("B")
    b.add("Y", 200)
    b.add("X", 100)
    assertFalse(a == b)

def _check_pl_str_duration():
    rock = _make_pl()
    pop = Playlist("Pop")
    pop.add("Blinding Lights", 200)
    merged = rock + pop
    s = str(merged)
    assertTrue("17:16" in s)
    assertTrue("3 songs" in s)

def _check_pl_str_songs():
    s = str(_make_pl())
    assertTrue("5:54" in s)
    assertTrue("8:02" in s)
    assertTrue("Bohemian Rhapsody" in s)


runner.run_tests("Playlist", Playlist, playlist_tests)


vector_tests = [
    ("str", lambda: (
        assertEqual(str(Vector(3, 4)), "Vector(3, 4)")
    )),
    ("repr", lambda: (
        assertEqual(repr(Vector(3, 4)), "Vector(3, 4)")
    )),
    ("str negative", lambda: (
        assertEqual(str(Vector(-1, -2)), "Vector(-1, -2)")
    )),
    ("eq same", lambda: (
        assertTrue(Vector(3, 4) == Vector(3, 4))
    )),
    ("eq different", lambda: (
        assertFalse(Vector(3, 4) == Vector(1, 2))
    )),
    ("add", lambda: (
        assertEqual(str(Vector(3, 4) + Vector(1, 2)), "Vector(4, 6)")
    )),
    ("sub", lambda: (
        assertEqual(str(Vector(3, 4) - Vector(1, 2)), "Vector(2, 2)")
    )),
    ("mul", lambda: (
        assertEqual(str(Vector(3, 4) * 3), "Vector(9, 12)")
    )),
    ("mul by zero", lambda: (
        assertEqual(str(Vector(3, 4) * 0), "Vector(0, 0)")
    )),
    ("abs 3-4-5", lambda: (
        assertEqual(abs(Vector(3, 4)), 5.0)
    )),
    ("abs zero", lambda: (
        assertEqual(abs(Vector(0, 0)), 0.0)
    )),
    ("abs irrational", lambda: (
        assertTrue(math.isclose(abs(Vector(1, 1)), math.sqrt(2)))
    )),
    ("lt by magnitude", lambda: (
        assertTrue(Vector(1, 2) < Vector(3, 4))
    )),
    ("lt equal magnitude", lambda: (
        assertFalse(Vector(3, 4) < Vector(3, 4))
    )),
    ("bool nonzero", lambda: (
        assertTrue(bool(Vector(1, 0)))
    )),
    ("bool zero", lambda: (
        assertFalse(bool(Vector(0, 0)))
    )),
    ("add does not mutate", lambda: (
        _check_vec_no_mutate()
    )),
    ("sorted by magnitude", lambda: (
        _check_vec_sorted()
    )),
]


def _check_vec_no_mutate():
    a = Vector(3, 4)
    _ = a + Vector(1, 1)
    assertEqual(str(a), "Vector(3, 4)")

def _check_vec_sorted():
    vecs = [Vector(5, 0), Vector(1, 1), Vector(3, 4)]
    mags = [abs(v) for v in sorted(vecs)]
    assertEqual(mags, sorted(mags))


runner.run_tests("Vector", Vector, vector_tests)


if __name__ == "__main__":
    runner.print_report()