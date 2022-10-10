from gettext import install
from setuptools import setup
from typing import List,Dict,OrderedDict

# declaring variables for setup functions
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "ROHIT"
DESCRIPTION = "THIS PROJECT HAS BEEN CREATED FOR HOUSE PREDICTION"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description:This function is going to return the list of requirements from requirements.txt

    return : Library names in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines



setup(

name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires= get_requirements_list()

)

if __name__=="__main__":