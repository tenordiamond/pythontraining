#Input validation with isalpha
#git test
catNames = []
while True:
	name = input('Enter the name of cat ' + str(len(catNames) +1) + ' (or type quit to stop.):')
	if name.isalpha():
		if name == "quit":
			break
		catNames = catNames + [name] #concat list
	else:
		print("Enter a valid string")
print('The catnames  you entered are:')
for name in catNames:
	print(' ' + name)
