# Stack OverFlow
print()
line = "I like to play guitar and piano and drums"
words = line.split()
print(words)
letters = [word[0] for word in words]
print(letters)
print ("".join(letters))
print()


# Coursera

def initials(phrase):
    words = phrase.split()
    result = ""
    letters=[word[0] for word in words]
    result += result.join(letters)
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS