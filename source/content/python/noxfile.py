"""
To run:

$ nox -s lint      # Runs flake8 and black, in Python 3.9 only

$ nox -s run_tests # Runs "pytest --html=report.html" for Python 3.7 and Python 3.9

In each case, nox generates a new virtual environment. There are flags that allow you
to reuse environments, but if you are willing to wait longer, recreating the env each
time will be a better guarantee that things will be reproducable.

When doing development, running "pytest" in your local environment can be a way of 
saving on the overhead of constructing a virtual env.
"""
import nox


@nox.session(python=["3.7", "3.9"])
def run_tests(session):
    session.install('-r', 'requirements.txt')
    session.install('pytest')
    session.run('pytest', '--html=report.html')


@nox.session(python=["3.9"])
def lint(session):
    session.install('black')
    session.install('flake8')
    session.run('flake8', '.')
    session.run('black', '.')

