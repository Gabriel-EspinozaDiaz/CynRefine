import re

string = 'Part:BBa C0040 - parts.igem.org\n\n\n dummytext \n\n\n Part:BBa_C0040\n                Designed by: Andrea Laurentius    Group: iGEM18_UI_Indonesia    (2018-09-25)'
nstring = re.findall(r'Designed by: (.*\w).*Group:',string)


string2 = 'Part:BBa C0040 - parts.igem.org\n\n\n dummytext \n\n\n Part:BBa_C0040\n                Designed by: June Rhee, Connie Tao, Ty Thomson, Louis Waldman.    Group: Antiquity'
nstring2 = re.findall(r'Designed by: (.*\w).*Group:',string2)
print(nstring)
print(nstring2)
