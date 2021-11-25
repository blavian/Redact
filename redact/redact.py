import re


filename = "/Users/beny.lavian/Desktop/supervisord.txt"
output = "/Users/beny.lavian/Desktop/working.txt"

with open(filename, 'r') as infile:
    lines = infile.readlines()
with open(output, 'w') as outfile:
        for line in lines:
            new_line = re.sub(
                r'1\d{10}',"redacted", "line"
            )
            outfile.write(new_line)
