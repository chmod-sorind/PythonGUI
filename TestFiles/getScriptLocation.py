import os
import sys


pathname = os.path.dirname(sys.argv[0])
print('path =', pathname)
print('full path =', os.path.abspath(pathname))
