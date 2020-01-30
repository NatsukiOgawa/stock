import os
import time

now = time.time()
# os.system('git add *')
# os.system('git commit -m "test commit"')
os.system('git add *')
os.system('git commit -m "{}"'.format(now))
os.system('git push')
# os.system('git push')
