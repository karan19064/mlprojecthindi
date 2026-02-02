from setuptools import setup, find_packages

setup(
    name="mlproject",
    version="0.1.0",
    author='karan',
    author_email='karanpanchamiya4@gmail.com',
    packages=find_packages(),
    install_requires=['numpy', 'pandas', 'scikit-learn', 'flask']
)
