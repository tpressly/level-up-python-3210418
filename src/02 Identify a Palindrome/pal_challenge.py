# Python Code Challenge #2: Identify a Palindrome
# Your goal is to implement a function, 
# `is_palindrome()`, that takes a text string 
# as the input argument and returns a boolean 
# indicating whether or not it's a palindrome.

def is_palindrome(myString):
  myString = cleanString(myString)
  print(myString)
  revString = myString[::-1]
  result = False
  if revString == myString: result = True
  return result

def cleanString(myString):
  myString = myString.upper()
  newString=''
  for i in myString:
    if ord(i) > 64 and ord(i) < 91:
      newString = newString + i
  return newString


print(is_palindrome("Go hang a salami - I'm a lasagna hog."))