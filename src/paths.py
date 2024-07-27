'''
This setup is crucial for organizing project files and making sure that required directories are available before the project runs.
'''
#importing modules
from pathlib import Path
import os


#Defining Directory Paths
'''
PARENT_DIR:
- Path(__file__) refers to the path of the current script (paths.py).
- .parent moves up one directory level (to the directory containing paths.py).
- .resolve().parent ensures the path is absolute and then moves up another directory level (likely to the root directory of your project).

DATA_DIR:
- PARENT_DIR / 'data' constructs the path to the data directory inside the parent directory.

MODELS_DIR:
- PARENT_DIR / 'models' constructs the path to the models directory inside the parent directory.
'''
PARENT_DIR = Path(__file__).parent.resolve().parent
DATA_DIR = PARENT_DIR / 'data'
MODELS_DIR = PARENT_DIR / 'models'


#Ensuring Directory Existence
if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)

if not Path(MODELS_DIR).exists():
    os.mkdir(MODELS_DIR)