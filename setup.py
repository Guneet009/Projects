from setuptools import find_packages,setup
from typing import List

const1 = '-e .'

def get_requirements(file_path:str)-> List[str]:
    """
    this function will return requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if const1 in requirements:
            requirements.remove(const1)
        

        
setup(
name = 'MLproject',
version='0.0.1',    
author='Guneet',
author_email='guneet1308@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')
)


'''

this file is used to install requirements
it helps to build and distribute python pakage
the above information is used by pip tool which will help to install package
with the help of this you can build and distribute your python pakage for others to use
In Python projects, if you create a file called __init__.py in a directory then Python will treat that directory as a package 

'''