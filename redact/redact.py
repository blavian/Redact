import re


filename = "/Users/beny.lavian/Desktop/supervisord.txt"
output = "/Users/beny.lavian/Desktop/working.txt"

with open(filename, 'r') as infile:
    lines = infile.readlines()
    pattern = re.compile(r'1\d{10}')
    print(pattern)

with open(output, 'w') as outfile:
        for line in lines:
            match = re.match(pattern,line)
            if match:
                newline = re.sub(pattern, "redacted", line)
            else:
                outfile.write(line)


                
