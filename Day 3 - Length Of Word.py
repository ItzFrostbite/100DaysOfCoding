print("Enter word to get length:")
word = input()

lengthOfWord = (len(word))
print(lengthOfWord, "Letters")

print("Would you like to go again [Y/N]")
again = input()

if again == "Y" or again == "y":
    print("Enter word to get length: ")
    word = input()
    lengthOfWord = (len(word))
    print(lengthOfWord, "Letters")
elif again == "N" or again == "n":
    print("Ok bye...")
    bye = input()
    quit()
else:
    print("Invalid Response")
    bye = input()
    quit()

while again != "N":
    print("Would you like to go again [Y/N]")
    again = input()
    if again == "N" or again == "n":
        print("Ok bye...")
        bye = input()
        quit()
    elif again == "Y" or again == "y":
        print("Enter word to get length: ")
        word = input()
        lengthOfWord = (len(word))
        print(lengthOfWord, "Letters")
    else:
        print("Invalid Response")
        bye = input()
        quit()


print("Enter word to get length: ")
word = input()
lengthOfWord = (len(word))
print(lengthOfWord, "Letters")
