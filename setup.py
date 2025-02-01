'''
The Setup.py file is essential part of packaging and distributing 
python projects . It is used by setuptools (or distutils in older python versions) to
define the configuration of the project, such as metadata, dependencies, and more.

'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements.

    '''
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # Read lines from file
            lines = file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## Ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")         

    return requirement_lst            

setup(
    name = "Network Security",
    version = "0.0.1",
    author= "Jagannath Nayak",
    author_email= "jagannath08108nayak@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements()
)   

