import sys
import os

def resource_path(relative_path):
    try:
        return os.path.join(sys._MEIPASS, relative_path)
    except AttributeError:
        return os.path.abspath(relative_path)