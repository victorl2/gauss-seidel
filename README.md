# Solving linear equation problems

This project implements the **Gauss Jacobi** and **Gauss Seidel** methods for *solving linear equations*, the methods use the **compressed sparse matrix** structure to store only non zero values present in the matrices.

# How to run 
+ You must have python 2.5+ installed
+ Install the required dependencies present in the **requirements.txt** running `pip install -r requirements.txt` inside the project folder
+ Inside the `src`folder you can find two files **gauss_jacobi.py** and **gauss_seidel.py**
+ You can run each file with `python gauss_jacobi.py` and `python gauss_seidel.py`
+ You can also edit the example problem inside each file for testing

# Running tests
+ Make sure the `requirements.txt` was installed in your python.
+ Inside the **src** folder run `python -m pytest tests/`
