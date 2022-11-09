def fahrenheit_to_celsius(find_range):
    
    for value in range (0, find_range+1, 10):
        Celsius = (value-32)*(5/9)
        print("{:>3} F | {:>6.2f} C".format(value, Celsius))
    

fahrenheit_to_celsius(100)