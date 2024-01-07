from setuptools import setup , find_packages 
import os 
import sys 

HYPEN_DOT = "-e ."

def get_requirements(file):

    with open(file) as f:
        data = f.readlines()
        data = [i.replace("\n" , "") for i in data]

        if HYPEN_DOT in data :
            data.remove(HYPEN_DOT)
        
    return data 

setup(

    name = "DoorDashProject",
    version = "0.0.1",
    author = "Faisal",
    author_email = "thefaisalshaikh@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt') # txt file 

)