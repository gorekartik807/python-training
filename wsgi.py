import sys

# Apna username aur folder path daal
path = '/home/kartik/python-training'  # ya /home/YourUsername/mysite
if path not in sys.path:
    sys.path.append(path)

from app import app as application