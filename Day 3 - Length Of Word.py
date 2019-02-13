print("Enter word to get length:")
word = input()

lengthOfWord = (len(word))
print(lengthOfWord, "Letters")

print("Would you like to go again [Y/N]")
again = input()

if again == "Y":
    print("Enter word to get length: ")
    word = input()
    lengthOfWord = (len(word))
    print(lengthOfWord, "Letters")
    if again == "N":
        print("Ok bye...")
        bye = input()
        quit()
    if again == "n":
        print("Ok bye...")
        bye = input()
        quit()

#Lower Case y and n start

if again == "y":
    print("Enter word to get length: ")
    word = input()
    lengthOfWord = (len(word))
    print(lengthOfWord, "Letters")
    if again == "N":
        print("Ok bye...")
        bye = input()
        quit()
    if again == "n":
        print("Ok bye...")
        bye = input()
        quit()


if again == "n":
    print("Ok bye...")
    bye = input()
    quit()

#Lower Case y and n end

if again == "N":
    print("Ok bye...")
    bye = input()
    quit()

while again != "N":
    print("Would you like to go again [Y/N]")
    again = input()
    if again == "N":
        print("Ok bye...")
        bye = input()
        quit()
    if again == "n":
        print("Ok bye...")
        bye = input()
        quit()
    print("Enter word to get length: ")
    word = input()
    lengthOfWord = (len(word))
    print(lengthOfWord, "Letters")
