# Try out the enumerate function for yourself in this quick exercise. 
# Complete the skip_elements function to return every other element from the list, 
# this time using the enumerate function to check if an element is on an even position or an odd position.

def skip_elements(elements):
	new_elements = []
	for index, element in enumerate(elements):
		if index%2 == 0:
			#print(element)
			new_elements.append(elements[index])
            # new_elements = new_elements + [elements[index]] ::: (does the same thing as above line)
		
	
	return new_elements

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']