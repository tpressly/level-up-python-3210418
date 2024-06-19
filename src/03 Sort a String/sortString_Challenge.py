
# function to sort the words in a string and return the sorted string.
# ignore case when sorting

def sort_words(myString):
    myList = myString.split(' ')
    # print(myList)
    myList = sorted(myList, key=str.casefold)
    # print(myList)
    return (' '.join(myList))


#def make_List(myString):
#    myList = myString.split(' ')
#    return myList

#def list(myList):
#    def __lt__(myList):
#        ulist = list.lower()
#        umyList = list.upper()
#        return ulist < umyList

print(sort_words('string of words'))
print(sort_words('banana ORANGE apple'))
