# Homework 4

## 3 Levels Of Calculator Homework

### Functionality
1. Uses the faker library to generate fake test data.
2. Accepts user input.

### Testing
1. pytest --pylint --cov

2. pytest --num_records=100
3. pytest tests/test_main.py
4. pytest --num_records=100 tests/test_calculation.py

5. python main.py 10 5 add
6. python main.py 22 8 subtract
7. python main.py 3 4 multiply
8. python main.py 50 2 divide
9. python main.py 2 0 divide
