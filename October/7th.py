# Write a Python program that accepts a filename from the user and prints the extension of the file.
a= input("Enter the file name and extension-:")
extension_name = a.split('.')
if len(extension_name)>1:
    print(extension_name[-1])
else:
    print("Nothing found")