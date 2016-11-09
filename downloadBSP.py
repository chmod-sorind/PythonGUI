#!C:\Python27\python.exe
import argparse
import os
import re
import subprocess
import urllib.request
import sys


# Arguments
parser = argparse.ArgumentParser(description='Download specified package from link/URL and installs it.')
parser.add_argument('url', metavar='URL', type=str, nargs='?', help='The Link/URL to target package.')
args = parser.parse_args()

# Get the name of the package.
def getPakageName(link):
    regex = re.compile(r'\w{9}\%\d{2}\w{6}-\d{2}_\d{1,2}_\d{1,2}-\d{1,5}.\w{3}')
    matches = re.findall(regex, link)
    return matches[0].replace("%20", "_")


getPakageName(args.url)
packageName = getPakageName(args.url)


def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r" + packageName + "...%d%%" % percent)
    sys.stdout.flush()


urllib.request.urlretrieve(args.url, packageName, reporthook=dlProgress)


# Kill bsp process if open.
if b'bsp.exe' in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]:
    os.system("taskkill /F /im bspsh.exe")
    os.system("taskkill /F /im bsp.exe")
    print('"SUCCESS: The process "bsp.exe" with has been terminated."')
else:
    print('\n"ERROR: The process "bsp.exe" not found."')

# Install package
logName = packageName.replace(".msi", ".log")
askForLog = input('Generate a install log? (Yes/No) \n')
if askForLog.lower() in ('y', 'yes'):
    try:
        os.system("msiexec /i {} /qn /l*v {}".format(packageName, logName))
    except WindowsError as e:
        print(e)
elif askForLog.lower() in ('n', 'no'):
    print('Cool, No logs then..')
    try:
        os.system("msiexec /i %s /qn" % packageName)
    except WindowsError as e:
        print(e)
print("Done!")
# time.sleep(10)
# with open(logName) as log:
#     for line in log:
#         print(line)
