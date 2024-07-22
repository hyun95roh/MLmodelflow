from setuptools import find_packages, setup

with open("README.md", "r") as mlmf:
    long_description = mlmf.read()

setup(
    name="MLmodelflow",
    version="0.0.1",
    license="MIT",
    author="hyun95roh",
    author_email="hroh@usc.edu",
    description="Model flow chart on the Scikit-learn",
    long_description=long_description,
    packages=find_packages(),
    setup_requires=["setuptools_scm"],
    url="https://github.com/hyun95roh/ml_Modelflow",
    python_requires='>=3.8',
    install_requires=[
        "pandas",
        "numpy",
    ],
)