from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    '''
    Returns a list of requirements from the requirements.txt file.
    '''
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt') as file:
            # Read lines from the file
            lines=file.readlines()
            #Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
               
    except FileNotFoundError:
        print("requirements.txt file not found.")
    return requirement_lst

setup(
    name='NetworkSecurityProject',
    version='0.0.1',
    author='Aryan',
    author_email="aryanmallick87@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)