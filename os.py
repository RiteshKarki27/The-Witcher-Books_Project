import os
from os import listdir, rename
from os.path import isfile, join

mypath = input("Enter the path where all the downloaded files are stored")
print(mypath)

path_converted = join(mypath, 'Converted')
##os.mkdir(path_converted)
print(path_converted)

path_processed = join(mypath, 'Processed')
##os.mkdir(path_processed)
print(path_processed)
