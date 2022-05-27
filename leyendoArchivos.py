import os

basePath="my_directory/"

with os.scandir(basePath) as entries:
    for i in entries:
        if i.is_file():
            print(i.name)
            