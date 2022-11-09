# Given a list of filenames, 
# we want to rename all the files with extension "hpp" to the extension "h". 
# To do this, we would like to generate a new list called newfilenames, 
# consisting of the new filenames. 
# Fill in the blanks in the code using any of the methods you’ve learned thus far, 
# like a for loop or a list comprehension.


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
new_filenames= []
# using as many lines of code as your chosen method requires.

# Loop based solution:::
for files in filenames:
    if files[-3:]=="hpp":       
        new_filenames.append(files.replace("hpp","h"))
    elif files[-3:] !=0:
        new_filenames.append(files) 
       
# Alternative Sol::: using list comprehension
alt_filenames = [files.replace(".hpp",".h") for files in filenames]

print(new_filenames) 
print()
print(alt_filenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]