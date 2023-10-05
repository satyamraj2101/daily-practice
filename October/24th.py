#  Write a Python program to test whether a passed letter is a vowel or not.

def Vowel(letter):
    box = ["a"," e", "i", "o", 'u']
    if letter in box:
        return "Vowel"
    else:
        return "Not Vowel"


print(Vowel("a"))