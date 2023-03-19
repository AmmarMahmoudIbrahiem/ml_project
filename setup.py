from setuptools import find_packages,setup
from typing import List

HYPER_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this funcation return the list of requirmants 
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readline()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)
    return requirements


setup(
name='ml_project',
version='0.0.1',
author='AmmarMahmoudIbrahiem',
author_email='ammar013783@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)