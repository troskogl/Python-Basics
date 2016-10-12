import urllib
import time
import re

what = "enellerannentext"
page = urllib.urlopen("http://gjerrigknark.com/")
text = page.read()
another = "Y"
# print(text)

def FindInText(findwhat):
	for m in re.finditer(findwhat, text):
		print (findwhat, m.start(), m.end())


while another == "Y" or another == "y":
	findwhat = raw_input ("What to search for? ")
	FindInText(findwhat)
	another = raw_input("Make another? (Y/y) ")




#	print (findwhat)
#	index = text.find(findwhat)
#	subtext = text[index:index+10]
#	print(subtext.upper())