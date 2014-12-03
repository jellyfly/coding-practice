# reference https://docs.python.org/2/library/subprocess.html

from subprocess import call
from subprocess import check_output
import os

print (os.getcwd())
os.chdir('C:\\')
print (os.getcwd())
os.chdir('C:\\Users\\mintan2\\Desktop\\PCC\\pcc-cisco\\database')
print (os.getcwd())


call("dir", shell = True)
call("type"+" extract_features.py", shell=True)

out = check_output("dir C:", shell=True)
print (out)
