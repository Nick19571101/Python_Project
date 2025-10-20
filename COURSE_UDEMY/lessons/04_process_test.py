import os
import subprocess

x = subprocess.Popen(['ping', 'google.com', '-c', '2'])

print(x.args)
print('Next code')
