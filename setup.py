from setuptools import setup, find_packages

setup(
    author='Juan Emilio Zurita Macias',
    author_email='juanezm@ieee.org',
    name='wordcounter',
    version='0.1',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.5, <4',
    install_requires=['click==7.1.2', 'pytest==6.1.2'],
    entry_points={
        'console_scripts': ['wordcounter-cli=wordcounter.entrypoints.cli:main'],
    }
)
