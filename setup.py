from setuptools import find_packages,setup  #setup is use find the package inside folder src and install the rquirements .txt file
from typing import List  # output as list in function 


#this function is used to read list packages the requirements txt file and install the packages
HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


# this is metadata of the project  and its constant 
setup(
project_name="ML_project_setup_tutorial",
version="0.0.1",
author="LathaKH",
author_emial="lathakh2018@gmail.com",
packages=find_packages(),
install_requirements=get_requirements("requirements.txt")

)
