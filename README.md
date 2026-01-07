# PYTHON — Learning Programs & Notes

A personal collection of **Python practice programs**, topic-wise examples, and a small **NumPy notebook**. The goal of this repo is to keep short, focused code snippets for quick revision and experimentation.

> This is a learning repository (not a packaged library). Most files are meant to be run directly.

## What's inside

- **Core Python basics**: operators, conditionals, loops, strings, lists/tuples, sets, dictionaries, functions
- **OOP**: classes, constructors, inheritance, operator overloading
- **Advanced concepts**: decorators, dunder methods, args/kwargs, walrus operator, map/filter/reduce, errors
- **Files & OS utilities**: read/write/append, context managers, `os`, `shutil`, CSV reading
- **Mini scripts**:
	- `number_guesser.py` — interactive number guessing (binary-search style)
	- `reaminder.py` — desktop notification reminder (uses `plyer`)
- **Notebook**:
	- `numpy.ipynb` — NumPy basics (arrays, reshape, slicing, 2D indexing)

## Folder map

The repo is organized by topic:

- `1_operators/` — arithmetic, assignment, comparison, logical ops, if/else, ternary
- `3_loops/` — for/while loops, factorial, patterns, palindrome, etc.
- `4_functions/` — arguments, recursion, modules, globals, docstrings
- `5_string/` — indexing, slicing, f-strings, basics
- `6_lists/` — list operations, methods, comprehensions, tuples
- `7_sets/` — sets + set operations, plus dictionary examples
- `9_oops/` — OOP examples (class, constructors, inheritance, operator overloading)
- `10_py_adv_concepts/` — decorators, dunder, args/kwargs, map/filter/reduce, error handling
- `11_files/` — file handling examples + practice files
- `sql/` — small Python + SQL-related experiments

Top-level scripts you may want to try:

- `number_guesser.py`
- `reaminder.py`
- `a.py` (scratchpad of small problems)

## Requirements

### Python

- Python **3.8+** recommended

### Dependencies

Not all scripts need external packages.

- `numpy.ipynb` requires:
	- `numpy`
- `reaminder.py` requires:
	- `plyer`

If you don't have them installed, install with:

```powershell
python -m pip install numpy plyer
```

## How to run

### Run a Python script

From the repo folder:

```powershell
python .\number_guesser.py
```

### Run the reminder script

```powershell
python .\reaminder.py
```

> Note: This script sends a desktop notification every hour in an infinite loop. Stop it with **Ctrl + C**.

### Open the NumPy notebook

Open `numpy.ipynb` in **VS Code** (Jupyter extension) and run cells.

## Notes / conventions

- Most files are small and focused on a single concept.
- Some filenames contain typos (kept as-is from practice).
- Many examples use `input()` and are interactive.

## Suggested learning path

1. `1_operators/`
2. `3_loops/`
3. `5_string/`, `6_lists/`, `7_sets/`
4. `4_functions/`
5. `9_oops/`
6. `10_py_adv_concepts/`
7. `11_files/`
8. `numpy.ipynb`

## License

If you plan to share this publicly, add a license file (MIT is common for learning repos).