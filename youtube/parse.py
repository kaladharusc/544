import collections, os
import re

def parse():
    files = os.listdir("/Users/kaladhar/Desktop/casey/")
    contents = ""
    for file in files:
        f = open("/Users/kaladhar/Desktop/casey/" + file, "r")
        contents = contents + f.read()
    newContents = contents.replace("\r\n", " ")
    pattern = re.compile(r'airport', re.IGNORECASE)
    freqs = collections.Counter(contents.split())
    #print(freqs)
    print(len(re.findall(pattern, contents)))
    print(re.findall(pattern, contents))

if __name__ == '__main__':
    parse()