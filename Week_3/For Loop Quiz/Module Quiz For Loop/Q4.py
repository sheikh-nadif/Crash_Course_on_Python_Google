# Write a script that prints the multiples of 7 between 0 and 100. 
# Print one multiple per line and avoid printing any numbers that aren't multiples of 7. 
# Remember that 0 is also a multiple of 7.

for i in range (0,101):
    if 7*i < 100 and (7*i)%7 ==0:
        print (7*i)

# Alternative
# num = 0
# mult = 7
# while num <= 100:
    # print(num)
    # num += mult