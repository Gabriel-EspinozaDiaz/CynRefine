import re

string = 'Released HQ 2013 Sample In stock 1 Registry Star 318 Uses 3 Twins Get This Part Coding tetR'
sample = 'In stock'
nstring = re.findall(sample+r' (\d*) Registry Star',string)
print(nstring)