#ordinal numbers

my_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
for number in my_numbers:
	if number == '1':
		print(number + "st")
	elif number == '2':
		print(number + "nd")
	elif number == '3':
		print(number + "rd")
	else:
		print(number + "th")


alien_0 = {}
alien_0['color'] = 'yellow'
alien_0['points'] = '5'
print(alien_0)

#Rivers

rivers = {'nile': 'egypt', 'mississippi': 'USA', 'siene': 'france', 'volga': 'russia'}
for r, c in rivers.items():
		print(r.title() + " is a river in " + c)

cool_rivers = ['joan rivers', 'old man river', 'mississippi', 'volga' ]
for river in cool_rivers:
	if river in rivers:
		print("Oh, " + river.title() + ", you are a body of water in " + rivers[river].upper() + "!")

	else:
		print(river + " so funny")

