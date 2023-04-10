import sys
import subprocess
import time

# sem muitos segredos. Roda um pip install. 
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
 'pysimpleGUI', 'numpy', 'pyserial', 'pydobot', 'flask_sqlalchemy'])

time.sleep(1)

print("--> libs instaladas")