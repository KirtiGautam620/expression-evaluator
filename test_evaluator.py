from evaluator import evaluate

valid_tests = [
    ("2 + 3", 5),
    ("10 - 4", 6),
    ("3 * 4", 12),
    ("8 / 2", 4),
    ("2 + 3 * 4", 14),
    ("(2 + 3) * 4", 20),
    ("10 - 3 - 2", 5),
    ("100 / 10 / 2", 5),
    ("2.5 * 4", 10),
    ("0.1 + 0.2", 0.3),
    (".5 + .5", 1),
    ("-5", -5),
    ("-5 + 3", -2),
    ("3 * -2", -6),
    ("-(2 + 3)", -5),
    ("--5", 5),
    ("2 - -3", 5),
    ("((1 + 2) * (3 + 4))", 21),
    ("2 + 3 * (4 - 1) / 3", 5),
    ("  7   *2 ", 14),
]

error_tests = [
    "",
    "2 +",
    "(2 + 3",
    "2 + 3)",
    "()",
    "* 2",
    "2 3",
    "abc",
    "2 + a",
    "1.2.3",
    "2 ^ 3",
]

passed = 0
failed = 0

for expr, expected in valid_tests:
    try:
        result = evaluate(expr)
        if abs(result - expected) < 1e-9:
            passed += 1
        else:
            print("FAIL:", repr(expr), "gave", result, "expected", expected)
            failed += 1
    except Exception as e:
        print("FAIL:", repr(expr), "raised", e)
        failed += 1

for expr in error_tests:
    try:
        result = evaluate(expr)
        print("FAIL:", repr(expr), "should give an error but gave", result)
        failed += 1
    except ValueError:
        passed += 1

for expr in ["5 / 0", "1 / (2 - 2)", "3 / 0.0"]:
    try:
        evaluate(expr)
        print("FAIL:", repr(expr), "should give division by zero")
        failed += 1
    except ZeroDivisionError:
        passed += 1

print(passed, "passed,", failed, "failed")
