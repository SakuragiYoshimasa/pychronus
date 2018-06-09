from setuptools import setup, find_packages, Extension


ext_modules = [
    Extension('pychronus',
              sources=['src/pychronus.py'])
]

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
    ext_modules=ext_modules,
    test_suite='tests',
)
