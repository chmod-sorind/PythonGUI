#!C:\Python35\python.exe

# ToDo: https://github.com/verigak/progress/

import argparse
import os
import re
import subprocess
import urllib.request
import sys
import time
from clint.textui import progress
import requests
import click
from progress.bar import Bar


# Arguments
parser = argparse.ArgumentParser(description='Download specified package from link/URL and installs it.')
parser.add_argument('url', metavar='URL', type=str, nargs='?', help='The Link/URL to target package.')
args = parser.parse_args()





# Get the name of the package.
def getPakageName(link):
    regex = re.compile(r'\w{9}%\d{2}\w{6}-\d{2}_\d{1,2}_\d{1,2}-\d{1,5}.\w{3}')
    matches = re.findall(regex, link)
    return matches[0].replace("%20", "_")

try:
    #getPakageName(args.url)
    packageName = getPakageName(args.url)
except Exception as e:
    sys.exit("ERROR: 404. No package Found.")


# r = requests.get(args.url, stream=True)
# path = '/some/path/for/file.txt'
# with open(packageName, 'wb') as f:
#     total_length = int(r.headers.get('content-length'))
#     for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1):
#         if chunk:
#             f.write(chunk)
#             f.flush()


bar = Bar('processing', max=10)
for i in range(10):
    try:
        urllib.request.urlretrieve(args.url, packageName)
        print('')
    except Exception as e:
        print(e)
    bar.next()
bar.finish()

def dlProgress(count, blockSize, totalSize):
    percent = int(count * blockSize * 100 / totalSize)
    sys.stdout.write("\r" + packageName + " > %d%%" % percent)
    sys.stdout.flush()

# try:
#     urllib.request.urlretrieve(args.url, packageName, reporthook=dlProgress)
#     print('')
# except Exception as e:
#     print(e)

# Kill bsp process if open.
if b'bsp.exe' in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]:
    try:
        os.system("taskkill /F /im bspsh.exe")
        os.system("taskkill /F /im bsp.exe")
        print('"SUCCESS: The process "bsp.exe" with has been terminated."')
    except Exception as e:
        print(e)
else:
    print('SKIP: The process "bsp.exe" not found.')

# Install package
logName = packageName.replace(".msi", "_Install.log")
# askForLog = input('Generate a install log? (Yes/No) \n')
# askForLog = "yes"
# if askForLog.lower() in ('y', 'yes'):
try:
    print("{} installing...".format(packageName))
    os.system("msiexec /i {} /qb /l*v {}".format(packageName, logName))
    print("{} successfully installed".format(packageName))
except WindowsError as e:
    print(e)
# elif askForLog.lower() in ('n', 'no'):
#     print('Cool, No logs then..')
#     try:
#         os.system("msiexec /i %s /qn" % packageName)
#     except WindowsError as e:
#         print(e)

print("Start cleaning...")
try:
    os.system("del /F {}".format(packageName))
except Exception as e:
    print(e)


print("Dedicate te player...")
try:
    cmdline = r'C:\"Program Files (x86)"\BroadSign\bsp\bin\bsp_dedicate.exe'
    os.system(cmdline + " --dedicate")
    print("Successfully setup dedicatet player.")
except Exception as e:
    print(e)


askRestart = input("Reboot the System? (Yes/No) \n")
if askRestart.lower() in ('y', 'yes'):
    try:
        print("System is now restarting.\n")
        time.sleep(1)
        os.system("shutdown.exe /f /r /t 0")
    except WindowsError as e:
        print(e)
elif askRestart.lower() in ('n', 'no'):
    print("** A reboot is required for the changes to take effect **")
