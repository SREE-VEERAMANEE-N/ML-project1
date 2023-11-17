from setuptools import find_packages, setup
from typing import List



def get_requirements(file_path: str )-> List[str]:
    '''
    thiis function will return list of requirements
    '''

    requirements  = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if 'HYPEN_E_DOT' in requirements:
            requirements.remove('HYPEN_E_DOT')





setup (
    name =  'mlprojects',
    version= '0.0.1',
    author= 'veera',
    author_email= 'sreeveerasree@gmail.com',
    packages= find_packages(),

    install_requires = get_requirements('requirements.txt')


     
)