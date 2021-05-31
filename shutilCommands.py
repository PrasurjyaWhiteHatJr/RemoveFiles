import os
import shutil
path = "c:/users/user/Documents/Class99"
print("beforeCopyingFile")
print(os.listdir(path))
source = "c:/users/user/Documents/Class99/folder1/File.txt"
destination = "c:/users/user/Documents/Class99/folder2/File.txt"
dest = shutil.move(source, destination)
print("afterCopying")
print(os.listdir(path))