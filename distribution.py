"""
distribution.py
Author: Daniel Melnikov
Credit: Myself, Mr. Dennison, Overstack.com, internet

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
from collections import defaultdict
from operator import itemgetter
import string
letterNumdict=defaultdict(list)
alphabet=string.ascii_lowercase
#sentence=input("Please enter a string of text (the bigger the better): ")
sentence="The rain in Spain stays mainly in the plain."
lowercaseSentence=sentence.lower()
for l in alphabet:
    numberofLetters=lowercaseSentence.count(l)
    if numberofLetters>0:
        letterNumdict[numberofLetters].append(l)
        #letterNumdict[numberofLetters]=x
        #print(x*numberofLetters)
for i in sorted(letterNumdict.items(),key=lambda x: x[0],reverse=True):
#    print(i)
#    k=i[1]
#    print(k)
    for z in i[1]:
        print(i[0]*z)























