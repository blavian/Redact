import re
string = "beny@gmail.com"
pattern= re.compile(
r'''
(^|\s|""|'|<)((1|")?\d{10}[^,\.](")?(")?\b
|\d{3}-\d{3}-\d{4})
|(\(\d+\)\-\d{3}\-\d{4})
|(?<=mphone:)1\d{10}
|(?<=first_name['"]: )['"].*?['"]
|(?<=last_name['"]: )['"].*?['"]
|\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b
|(?<=['"]address1['"]: )['"](.*?)["'](\s|$|"|\))
'''
)
print(pattern)





