import os
path = "c:/users/user/Documents/Class99/File.txt"
root_ext = os.path.splitext(path)
print("rootPath", root_ext[0])
print("extensionPath", root_ext[1], "\n")