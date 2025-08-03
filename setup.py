from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name='vecalign',
    version='0.1.0', # Placeholder version
    py_modules=['vecalign'],
    ext_modules=cythonize(
        "*.pyx", # This will find and compile all .pyx files
        compiler_directives={'language_level' : "3"}
    ),
    install_requires=[
        'numpy>=1.19',
        'scipy>=1.0',
        'six>=1.0'
    ],
    include_dirs=[numpy.get_include()]
)
