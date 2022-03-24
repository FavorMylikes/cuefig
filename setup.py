from setuptools import setup, find_packages

setup(
    name='cuefig',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT License',
    author='麦丽素',
    author_email='l786112323@gmail.com',
    description='A config framework that you can cue and hint quickly.',
    data_files=[('cuefig/logger', ['cuefig/logger/logging.yaml'])],
)


