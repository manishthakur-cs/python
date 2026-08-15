import os

# Specify the directory path
directory = "/"   # Current directory

# Get and print the contents
contents = os.listdir(directory)

print("Contents of the directory:")
for item in contents:
    print(item)