import os
from configparser import ConfigParser

config = ConfigParser()
config.read("ext_conf.ini")

path = config.get("Exten", "path")
old_ext = config.get("Exten", "py")
new_ext = config.get("Exten", "text")

os.chdir(path)
os.getcwd()

for file in os.listdir():
	if file.endswith(py):
		print(file)
		new_name = file.rsplit(".",1)[0] +"."+ text
		print(new_name)
		os.rename(file, new_name)

************************************************

import os
resp = os.walk("C:\\Users\\l\\Desktop\\python")
d1 = {}

for r,d,f in resp:
	for file in f:
		d1.setdefault(file, []).append(r)

print (d1)
file_name = input("Enter the file name ")
for k,v in d1.items():
    if file_name.lower() in k.lower() :
        print (k,":", v)
        for find_file in v:
        	print(find_file)
