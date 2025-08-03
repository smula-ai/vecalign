from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# This explicitly defines the C extensions that need to be compiled.
ext_modules = [
    Extension('dp_utils', ['dp_utils.pyx'], include_dirs=[numpy.get_include()]),
    Extension('rf_utils', ['rf_utils.pyx'], include_dirs=[numpy.get_include()])
]

setup(
    name='vecalign',
    version='0.1.0', # Placeholder version
    ext_modules=cythonize(ext_modules),
    install_requires=[ # These are the runtime dependencies
        'numpy>=1.19',
        'scipy>=1.0',
        'six>=1.0'
    ]
)
