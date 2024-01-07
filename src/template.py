import os 
import sys 
from pathlib import Path 


list_of_files = [
    "\\src\\__init__.py",
    "\\src\\components\\__init__.py",
    "\\src\\components\\data_ingestion.py",
    "\\src\\components\\data_transformation.py",
    "\\src\\components\\model_trainer.py",
    "\\src\\utils.py",
    "\\src\\exception_file.py",
    "\\src\\logger.py",
    "\\src\\pipeline\\__init__.py",
    "\\src\\pipeline\\predicting_pipeline.py"

]

path_dir = os.getcwd() 

for file in list_of_files:

    full_path = path_dir + file 
    whole_path = Path(full_path)
    dir_path , file_name = os.path.split(whole_path)

    os.makedirs(dir_path, exist_ok=True)

    if os.path.exists(full_path):
        print(f"File Exists {file_name}")

    if (not os.path.exists(full_path)):
        with open(full_path , 'w') as f:
            print(f"File created {file_name}") 


    
