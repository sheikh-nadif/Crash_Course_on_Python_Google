file_dictionary= {"jpg":14, "png":15, "py":50, "csv":25, "docx":69}

# printing keys of file_dictionary
print(file_dictionary.keys())

# printing values of file_dictionary
print(file_dictionary.values())

# iterating over keys in dictionary
for file_names in file_dictionary:
    print(file_names)

# iterating over keys and values in dictionary (::: .items() is needed to get both key and value :::)
for extension, quantity in file_dictionary.items():
    print("There are {} files with {} extension".format(quantity, extension))