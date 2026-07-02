import sys
import os

# Project ka path add karo - ye change karna padega PythonAnywhere pe
path = '/home/yourusername/StudentMS'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application

# PythonAnywhere ko 'application' variable chahiye