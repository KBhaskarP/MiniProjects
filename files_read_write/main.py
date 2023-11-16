# file=open("files_read_write\example.txt") #use the relative path for accessing the contents of the file
# contents=file.read()
# print(contents)

# file.close() #This is used to manually close the file as the open file uses the resources of the computer.

#Way 2 

with open("files_read_write\example.txt") as f:
    contents=f.read()
    print(contents)
    
#Using this method we dont need to add the file.close() method

#there are basically three modes write as w read as r and append as a
#by mode=w we can write in the file, by mode="r" we can read the file, by mode="a" we can append what we change in the file.
#by mode="w" we can also create a new file if the file doesn't exist.

# with open("files_read_write\example.txt",mode="w") as f:
#     f.write("New Text") #This will basically overwrite the existing text in the file if we want dont want that we can set mode="a" for append 


# with open("files_read_write\example.txt",mode="w") as f:
#     f.write('''\nThis is a new line as I am using mode='a' for append rather than mode='w' for write
#             \n My name is Bhaskar I am writting this as the previous text got overwritten''')



# with open("new_file.txt",mode="w") as f:
#     f.write("New text written using mode='w' in a file which does not exist.\nThis will create a new file")

#This is possibe with mode ="w" only...