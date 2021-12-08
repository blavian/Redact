import re


filename = "/Users/beny.lavian/Desktop/supervisord.txt"
output = "/Users/beny.lavian/Desktop/test_redacted.txt"

with open(filename, 'r') as infile:
    lines = infile.readlines()
    pattern= re.compile(r'''(^|\s|""|'|<)((1|")?\d{10}[^,\.](")?(")?\b|\d{3}-\d{3}-\d{4})|(\(\d+\)\-\d{3}\-\d{4})|(?<=mphone:)1\d{10}|(?<=first_name['"]: )['"].*?['"]|(?<=last_name['"]: )['"].*?['"]|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b|(?<=['"]address1['"]: )['"](.*?)["'](\s|$|"|\))''')
# print(pattern)

with open(output, 'w') as outfile:
        for line in lines:
                newline = re.sub(pattern, "redacted", line)
                outfile.write(newline)


                
