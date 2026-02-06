from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            line = line.strip()
            if line and line != HYPEN_E_DOT:
                requirements.append(line)
    return requirements


setup(
    name="mlproject",
    version="0.1.0",
    author="karan",
    author_email="karanpanchamiya4@gmail.com",
    package_dir={"": "src"},                # ⭐ IMPORTANT
    packages=find_packages(where="src"),   # ⭐ IMPORTANT
    install_requires=get_requirements("requirements.txt"),
)
