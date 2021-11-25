import re


filename = "/Users/beny.lavian/Desktop/test.txt"
output = "/Users/beny.lavian/Desktop/test_redacted.txt"

with open(filename, 'r') as infile:
    lines = infile.readlines()

with open(output, 'w') as outfile:
        for line in lines:
                newline = re.sub(r"1\d{10}", "redacted", line)
                outfile.write(newline)


                
