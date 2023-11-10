from setuptools import setup, find_packages

setup(
    name='math_quiz',
    version='0.1.0',
    author='Hyeeun Park',
    author_email='ella.h.park@fau.de',
    packages=find_packages(include=['math_quiz', 'math_quiz.*'])
    )