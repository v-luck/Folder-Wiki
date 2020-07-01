import os
from datetime import datetime

print(os.getcwd())
os.chdir(os.getcwd() + "/Test")
print(os.getcwd())
print(datetime.now(tz=None))


