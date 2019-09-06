note : py37_ci


# Test circle-ci

1. conda install flake8 pytest pytest-cov
or pip install flake8 pytest pytest-cov

2. conda list --export > requirements.txt
or pip freeze > requirements.txt

3. test style
flake8 --statistics

4. pytest
pytest -v --cov

. 
