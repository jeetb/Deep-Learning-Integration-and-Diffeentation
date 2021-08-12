from string import digits, ascii_letters
import re

new_file = open("minialpha.train", "a+")
old_file = open("mini.train", "r")

f1 = old_file.readlines()

chars = set() 
 

for i in f1: #populating input equations and input chars
	#i = i.split('|')[1]
	
	toks = i.split()
	for tok in toks:
		chars.add(tok)

chars = list(chars)
chars.sort()
pre_dict = dict(zip(chars, list(digits+ascii_letters)))
post_dict = {v: k for k, v in pre_dict.items()}

print(chars)
print(pre_dict)
print(post_dict)

for i in f1:
#	if(count > 0):
		
	for key in sorted(pre_dict, key=len, reverse=True):
		i = i.replace(key, pre_dict[key])
		i = i.replace(' ', '')
	new_file.write(i)
	#else:
	#	break
	#count-=1
