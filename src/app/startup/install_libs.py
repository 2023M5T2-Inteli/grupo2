import sys
import subprocess
import time

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
 'pysimpleGUI', 'numpy', 'pyserial', 'pydobot', 'flask_sqlalchemy'])

time.sleep(1)

print("--> libs instaladas")