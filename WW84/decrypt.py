print("Hello, Themyscira!")
# This is a comment that won't be interpreted as a command.
# Associate the variable diana with the value "Wonder Woman 1984"
diana="Wonder Woman 1984"
# Print a message with the true identity of Diana
print("I believe Diana is actually "+diana)
# Define a power (fucntion) to chant a phrase
def chant(phrase):
    # glue three copies together and print it as a message
    print(phrase+phrase+phrase)
# Invoke the power chant on the phrase "Wonder Woman 1984!"
chant("Wonder Woman 1984! ")
def lassoLetter(letter,shiftAmount):
    letterCode=ord(letter.lower())
    aAscii=ord('a')
    alphabetSize=26
    trueLetterCode=aAscii + (((letterCode - aAscii) + shiftAmount) % alphabetSize)
    decodedLetter=chr(trueLetterCode)
    return decodedLetter