def factorial(n):
    #print("Factorial start with  "+ str(n))

    if n<2:
        #print("Returning Value:  1")
        return 1
    result = n * factorial(n-1)
    #print ("Returning Value:  "+ str(result) +"  for  "+ str(n))
    return result


inp = int(input("Enter a Digit:  "))
print ("Factorial of " + str(inp) + " is " +str(factorial(inp)))