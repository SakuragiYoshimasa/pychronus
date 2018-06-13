from setuptools import setup, find_packages, Extension

setup(
    name='pychronus',
    version='0.0.1',
    description='Python package for data handling',
    long_description='README.md',
    author='Yoshimasa Sakuragi',
    author_email='ysakuragi16@gmail.com',
    install_requires=[],
    url='https://github.com/SakuragiYoshimasa/pychronus',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests',
)
