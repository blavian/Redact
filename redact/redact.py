import re
import sys

filename= sys.argv[1]
output = sys.argv[2]

def main():
    with open(filename, 'r') as infile:
        lines = infile.readlines()
    with open(output, 'w') as outfile:
        for line in lines:
            re.sub()
            outfile.write(line)
