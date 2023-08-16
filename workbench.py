import re

string = '                Designed by: Andrea Laurentius    Group: iGEM18_UI_Indonesia    (2018-09-25)'
group = re.findall(r'Group: (.*?)\s',string)
date = re.findall(r'\((.*)\)',string)
print(group)
print(date)
