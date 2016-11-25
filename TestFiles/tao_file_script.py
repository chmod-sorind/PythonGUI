import re

def wordSearch(filename, word):
    pattern = re.compile(word)
    try:
        f = open(filename, 'r')
        for line in f.readlines():
            line = line.rstrip()
            content = re.findall(pattern, line)
            if len(content) > 0:
                print(line)
    except IOError as err:
        print("File error" + str(err))
    finally:
        f.close()


wordSearch('test.txt', 'test')
