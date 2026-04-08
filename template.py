import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


projectName = "cnnClassifier"

listOfFiles = [
    ".github/workflows/.gitkeep",
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/components/__init__.py",
    f"src/{projectName}/utils/__init__.py",
    f"src/{projectName}/config/__init__.py",
    f"src/{projectName}/config/configuration.py",
    f"src/{projectName}/pipline/__init__.py",
    f"src/{projectName}/entity/__init__.py",
    f"src/{projectName}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for filePath in listOfFiles:
    filePath = Path(filePath)
    filedir, filename = os.path.split(filePath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} and the file: {filename}")

    if(not os.path.exists(filePath)) or (os.path.getsize(filePath) != 0):
        with open(filePath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filePath}")
    else:
        logging.info(f"{filename} is already exist")