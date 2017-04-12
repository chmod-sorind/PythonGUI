<<<<<<< Updated upstream
#!C:\Python27\python.exe
=======
#!C:\Python35\python.exe

>>>>>>> Stashed changes
import argparse
import os
import re
import subprocess
import urllib.request
import sys
<<<<<<< Updated upstream
=======
import time
import ctypes
>>>>>>> Stashed changes


# Arguments
parser = argparse.ArgumentParser(description='Download specified package from link/URL and installs it.')
parser.add_argument('url', metavar='URL', type=str, nargs='?', help='The Link/URL to target package.')
args = parser.parse_args()
<<<<<<< Updated upstream
=======
url = args.url
>>>>>>> Stashed changes

# Get the name of the package.
def getPakageName(link):
    regex = re.compile(r'\w{9}\%\d{2}\w{6}-\d{2}_\d{1,2}_\d{1,2}-\d{1,5}.\w{3}')
    matches = re.findall(regex, link)
    return matches[0].replace("%20", "_")

<<<<<<< Updated upstream
=======

try:
    packageName = getPakageName(url)
except Exception as e:
    sys.exit("ERROR: 404. No package Found.")
>>>>>>> Stashed changes

getPakageName(args.url)
packageName = getPakageName(args.url)

<<<<<<< Updated upstream

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
=======
u = urllib.request.urlopen(url)
data_blocks = []
total = 0
meta = u.info()
metaInfo = str(meta).split()
print("Downloading package {0} of {1} bytes.".format(packageName, metaInfo[22]), flush=True)
fileTotalbytes = int(metaInfo[22])

while True:
    block = u.read(1024)
    data_blocks.append(block)
    total += len(block)
    hash = ((60*total)//fileTotalbytes)
    print("[{}{}] {}%".format('#' * hash, ' ' * (60-hash), int(total/fileTotalbytes*100)), end='\r', flush=True)
    if not len(block):
        break

data = b''.join(data_blocks)  # had to add b because I was joining bytes not strings
u.close()

sys.stdout.flush()

try:
    with open(packageName, "wb") as f:
        f.write(data)
except Exception as e:
    print(e)


# Kill bsp process if open.
if b'bsp.exe' in subprocess.Popen('tasklist', stdout=subprocess.PIPE).communicate()[0]:
    try:
        os.system("taskkill /F /im bspsh.exe")
        os.system("taskkill /F /im bsp.exe")
        print('"SUCCESS: The process "bsp.exe" with has been terminated."', flush=True)
    except Exception as e:
        print(e)
else:
    pass
    # print('SKIP: The process "bsp.exe" not found.')

# Install package
logName = packageName.replace(".msi", "_Install.log")
# askForLog = input('Generate a install log? (Yes/No) \n')
# askForLog = "yes"
# if askForLog.lower() in ('y', 'yes'):

try:
    print("\n{} installing...".format(packageName), flush=True)
    os.system("msiexec /i {} /qb /l*v {}".format(packageName, logName))
    print("{} successfully installed".format(packageName), flush=True)
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


print("Dedicate te player...", flush=True)
try:
    pathToExe = r'C:\"Program Files (x86)"\BroadSign\bsp\bin\bsp_dedicate.exe'
    os.system(pathToExe + " --dedicate")
    print("Successfully setup dedicated player.", flush=True)
except Exception as e:
    print(e)


askRestart = input("Reboot the System? (Yes/No) \n")
if askRestart.lower() in ('y', 'yes'):
    try:
        print("System is now restarting.\n", flush=True)
        time.sleep(1)
        os.system("shutdown.exe /f /r /t 0")
    except WindowsError as e:
        print(e)
elif askRestart.lower() in ('n', 'no'):
    print("** A reboot is required for the changes to take effect **", flush=True)
>>>>>>> Stashed changes
