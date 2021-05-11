import pathlib
from setuptools import find_packages, setup


HERE = pathlib.Path(__file__).parent
# README file text
README = (HERE / "README.md").read_text()

setup(
    name="pandas-data-dictionary",
    version="0.1.0",
    url="https://github.com/tcouch/pandas-data-dictionary",
    license='MIT',

    author="Tom Couch",
    author_email="t.couch@ucl.ac.uk",

    description="Pandas extension adding data dictionary accessor for describing and validating data.",
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=('tests',)),

    install_requires=["pandas", "numpy"],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
