import sys
import os
import fnmatch

if len(sys.argv)!=3:
	sys.exit("aguments and stuff is wrong num")
query=str(sys.argv[1])
loc=str(sys.argv[2])

for a,b,c in os.walk(loc):
	for fil in c:
		if fnmatch.fnmatch(fil, '*'+query+'*'):
			print(os.path.join(a, fil))		