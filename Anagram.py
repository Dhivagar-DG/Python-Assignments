def checkAnagram():
    words = input("Enter the two separate words ex:(word1 word2): ")
    wordsLst = words.strip().split() if len(words) > 0 else []

    if len(wordsLst) !=2:
        return "Validation"
    if len(wordsLst[0]) == len(wordsLst[1]):
        res = [i for i in wordsLst[0].upper() if i in wordsLst[1].upper() and i.isalpha()]
        return len(res) == len(wordsLst[0])
    return False

while True:
    finalRes = checkAnagram()
    if (finalRes == True):
        print(f"Given strings are 'Anagram'.".center(100, "*"))
    else:
        if finalRes != "Validation":
            print(f"Given strings are 'Not Anagram'.")
        else:
            print( "You must enter the two separate words ex:(Listen Silent)" )

    if finalRes != "Validation" and \
        (input("Press (x/X) to exit or enter other key to continue :").upper() == 'X'):
        break