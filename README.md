# SE-Lab-05
Repository containing all the materials for Software Engineering Lab 5.

**Known Issues Table**

| Issue | Type | Line(s) | Description | Fix Approach |
| :--- | :--- | :--- | :--- | :--- |
| **Use of eval**<br>(arbitrary code execution) | Security | 59 | `eval("print('eval used')")` can execute arbitrary code (Bandit B307, pylint W0123) | Remove `eval`;<br>implement explicit logic or use `ast.literal_eval` for literal parsing |
| **Mutable default argument** | Bug | 8 | `logs=[]` is a mutable default shared across calls (pylint W0102) | Change to `logs=None`<br>and inside function set `logs = [] if None` |
| **Missing input validation**<br>/ type checks | Bug | 8,51 | `addItem` accepts non-str item, non-int qty and negative qty (can corrupt state) | Validate types and ranges (raise `ValueError`);<br>coerce or reject invalid inputs |
| **getQty may raise KeyError** | Bug | 22,23 | `getQty` returns `stock_data[item]` without checking existence | Return `stock_data.get(item, 0)` or<br>raise a documented `KeyError` with clear message |
| **Bare except / silent pass** | Reliability /<br>Security | 19,20 | Bare `except` swallows all exceptions and hides errors (Bandit B110, flake8 E722) | Catch specific exceptions (e.g., `KeyError`) and log/handle them;<br>avoid broad `except: pass` |
| **Unsafe file handling**<br>(no context manager, no encoding) | Reliability /<br>Correctness | 26-34 | `open()` used without `with` and without `encoding`; manual `close` and `json.loads`/`read` can fail (pylint W1514, R1732) | Use `with open(file, mode, encoding="utf-8") as f` and `json.load()`/`json.dump()`;<br>handle I/O errors |


**Q&A:**

1.	Which issues were the easiest to fix, and which were the hardest? Why?
   
Easiest: Removing unused import, as it was just removing one line.

Hardest: Fixing global state across the module, as avoiding global rebinding required a design change and updating functions.

2.	Did the static analysis tools report any false positives? If so, describe one example.
   
Yes. The missing docstrings warnings (C0114/C0116) is an example. They are stylistic and not actual bugs. Similarly with the snake case and whitespace errors.

3.	How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
   
a) Local pre-commit hooks: Run flake8/pylint/bandit in pre-commit to block/flag commits with critical issues.

b) CI pipeline: Run bandit + flake8 + pylint (or a curated subset) in CI jobs; fail builds on security or high-severity findings, and report warnings for style issues.

4.	What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

Security: Removed arbitrary code execution vector (eval).

Robustness: Input validation prevents corrupting state and raises clear errors on misuse.

Reliability: Explicit exception handling prevents silent failures and file handling uses context managers to avoid resource leaks.
