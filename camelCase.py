# Camel Case

def camelCase():
    originalSentence = input("Enter your sentence: ")
    if originalSentence.isalnum() or originalSentence.isalnum():
        print("this is not a string character or a sentence, try again ! please :,(")
    else:
        newSentence = originalSentence.split()

        # use a for loop to check the sentence and modify to a lower case, and capitalize.
        for i in range(0, len(newSentence)):
            newSentence[i] = newSentence[i].lower()
            newSentence[i] = newSentence[i].capitalize()

        # here we join all the words and to print, we lower the first character.
        output = "".join(newSentence)

        sentenceCaCase = print(f' - {output[0].lower() + output[1:]} ')

        return sentenceCaCase
    
camelCase()

