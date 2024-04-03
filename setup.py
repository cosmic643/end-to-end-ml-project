from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function return a list of requirements
    '''
    requirements = []
    with open('requirements.txt','r') as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = 'mlproject',
    version = '0.0.1',
    author = 'cosmic',
    author_email = 'vaibhavkhamesra643@gmail.com',
    packages = find_packages(),
    #install_requires = ['numpy','pandas','seaborn']
    install_requires = get_requirements('requirements.txt')
)
