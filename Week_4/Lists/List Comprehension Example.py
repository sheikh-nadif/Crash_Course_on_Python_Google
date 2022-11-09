multiples = []
for x in range (1,11):
    multiples.append(x*7)

print(multiples)
print()

#Now with LIST COMPREHENSION
multiples=[x*7 for x in range(1,11)]
print(multiples)
print()

#Another example with string length
Language=["Python", "Java", "Oracle", "MySQL", "JavaScript", "C"]
Length = [len(language) for language in Language]
print(Language)
print(Length)