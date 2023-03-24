import sys
import subprocess
import time
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pysimpleGUI', 'numpy', 'pyserial'])

time.sleep(2)

print("TERMINOU DE INSTALAR!!!!")