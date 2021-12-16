from os import listdir, rename
from os.path import isfile, join
import subprocess


# return name of file to be kept after conversion.
# we are just changing the extension. mobi here.
def get_final_filename(f):
    f = f.split(".")
    filename = ".".join(f[0:-1])
    processed_file_name = filename+".mobi"
    return processed_file_name


# return file extension. pdf or epub or mobi
def get_file_extension(f):
    return f.split(".")[-1]


# list of extensions that needs to be ignored.
ignored_extensions = ["pdf"]

# here all the downloaded files are kept
mypath = "D:/The Witcher Books/The Witcher Source Files for Trial/"

# path where converted files are stored
mypath_converted = "D:\The Witcher Books\The Witcher Source Files for Trial\The Witcher Series Converted\\"

# path where processed files will be moved to, clearing the downloaded folder
mypath_processed = "D:\The Witcher Books\The Witcher Source Files for Trial\The Witcher Series Processed\\"

raw_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
converted_files =  [f for f in listdir(mypath_converted) if isfile(join(mypath_converted, f))]

for raw in raw_files:
    print(raw)
    
for conv in converted_files:
    print(conv)
    

for f in raw_files:
    final_file_name = get_final_filename(f)
    extension = get_file_extension(f)
    if final_file_name not in converted_files and extension not in ignored_extensions:
        print("Converting : "+f)
        try:
            subprocess.call(["ebook-convert",mypath+f,mypath_converted+final_file_name]) 
            s = rename(mypath+f, mypath_processed+f)
            print(s)
        except Exception as e:
            print('Hello')
            print('The error in printing file ' + f)
            print(e)
    else:
        print("Already exists : "+final_file_name)