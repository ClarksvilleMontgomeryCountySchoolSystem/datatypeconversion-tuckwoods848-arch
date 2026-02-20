"""
Consolidated tests for Data Type Conversion Tasks 1-4
Uses function-based pytest for GitHub Classroom compatibility
"""
import importlib
import re
import sys


# Task 1: Integer Conversion Tests
def test_task1_num_printed(capsys):
    """Task 1: Check that '25' is printed"""
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    importlib.reload(task1)
    captured = capsys.readouterr()
    assert "25" in captured.out, "Expected '25' to be printed"


def test_task1_type_printed(capsys):
    """Task 1: Check that 'str' is printed"""
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    importlib.reload(task1)
    captured = capsys.readouterr()
    assert "str" in captured.out, "Expected 'str' to be printed"


def test_task1_type_verification(capsys):
    """Task 1: Verify type str is shown"""
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    importlib.reload(task1)
    captured = capsys.readouterr()
    assert "str" in captured.out


def test_task1_result_correct(capsys):
    """Task 1: Check that '250' is printed"""
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    importlib.reload(task1)
    captured = capsys.readouterr()
    assert "250" in captured.out, "Expected '250' to be printed"


def test_task1_result_appears(capsys):
    """Task 1: Verify result 250 appears in output"""
    if 'task1' in sys.modules:
        del sys.modules['task1']
    import task1
    importlib.reload(task1)
    captured = capsys.readouterr()
    assert "250" in captured.out


# Task 2: Float Conversion Tests
def test_task2_price_printed(capsys):
    """Task 2: Check that '19.99' is printed"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    importlib.reload(task2)
    captured = capsys.readouterr()
    assert "19.99" in captured.out, "Expected '19.99' to be printed"


def test_task2_type_printed(capsys):
    """Task 2: Check that 'str' is printed"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    importlib.reload(task2)
    captured = capsys.readouterr()
    assert "str" in captured.out, "Expected 'str' to be printed"


def test_task2_type_verification(capsys):
    """Task 2: Verify type str is shown"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    importlib.reload(task2)
    captured = capsys.readouterr()
    assert "str" in captured.out


def test_task2_total_correct(capsys):
    """Task 2: Check that '24.99' is printed"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    importlib.reload(task2)
    captured = capsys.readouterr()
    assert "24.99" in captured.out, "Expected '24.99' to be printed"


def test_task2_total_appears(capsys):
    """Task 2: Verify total 24.99 appears in output"""
    if 'task2' in sys.modules:
        del sys.modules['task2']
    import task2
    importlib.reload(task2)
    captured = capsys.readouterr()
    assert "24.99" in captured.out


# Task 3: Type Conversion Variable Tests
def test_task3_a_is_float():
    """Task 3: Check that variable 'a' is a float"""
    if 'task3' in sys.modules:
        del sys.modules['task3']
    import task3
    importlib.reload(task3)
    assert isinstance(task3.a, float), "Variable 'a' should be a float"


def test_task3_b_is_string():
    """Task 3: Check that variable 'b' is a string"""
    if 'task3' in sys.modules:
        del sys.modules['task3']
    import task3
    importlib.reload(task3)
    assert isinstance(task3.b, str), "Variable 'b' should be a string"


def test_task3_c_is_int():
    """Task 3: Check that variable 'c' is an int"""
    if 'task3' in sys.modules:
        del sys.modules['task3']
    import task3
    importlib.reload(task3)
    assert isinstance(task3.c, int), "Variable 'c' should be an int"


def test_task3_d_is_int():
    """Task 3: Check that variable 'd' is an int"""
    if 'task3' in sys.modules:
        del sys.modules['task3']
    import task3
    importlib.reload(task3)
    assert isinstance(task3.d, int), "Variable 'd' should be an int"


def test_task3_e_is_string():
    """Task 3: Check that variable 'e' is a string"""
    if 'task3' in sys.modules:
        del sys.modules['task3']
    import task3
    importlib.reload(task3)
    assert isinstance(task3.e, str), "Variable 'e' should be a string"


def test_task3_f_is_float():
    """Task 3: Check that variable 'f' is a float"""
    if 'task3' in sys.modules:
        del sys.modules['task3']
    import task3
    importlib.reload(task3)
    assert isinstance(task3.f, float), "Variable 'f' should be a float"


# Task 4: Boolean Challenge (Extra Credit)
def test_task4_uses_bool_with_string():
    """Task 4: Check that bool() is called with an empty string or whitespace"""
    import re
    with open('task4.py', 'r') as f:
        code = f.read()
    # Pattern matches bool("") or bool(" ") or bool("   ") - only whitespace between quotes
    pattern = r'bool\s*\(\s*["\']\s*["\']\s*\)'
    assert re.search(pattern, code), "Must use bool() with an empty string or only whitespace, e.g., bool(\"\")"


def test_task4_found_false(capsys):
    """Task 4: Check that 'False' appears in output (extra credit)"""
    if 'task4' in sys.modules:
        del sys.modules['task4']
    import task4
    importlib.reload(task4)
    captured = capsys.readouterr()
    assert "False" in captured.out, "Expected 'False' to appear in output"
