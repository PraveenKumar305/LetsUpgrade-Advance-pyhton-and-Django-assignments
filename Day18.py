import os
root="G:\\LetsUpgrade\\Assignment"
for root,dir,files in os.walk(root):
  for s in files:
    path=root+"\\"+s
    print(path)

def find_string_in_file(f, string_to_find):
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False
    with open(f) as myFile:
        for num, line in enumerate(myFile, 1):
             if each in line:
               print('at line:', num)
