import os
import time

def checklogfile():
    # Check if log file exists
    fileName = r"docs/filelog.txt"
    existelogfile = os.path.isfile(fileName)

    if existelogfile:
        input('The log file already exists... ')
    else:
        try:
            with open('docs/filelog.txt', 'w') as f:
                f.write('Creating the log file!, ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        except FileNotFoundError:
            input("The 'docs' directory does not exist...")  
            
