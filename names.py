#friends list
friends = ['Perth', 'Bob', 'Boyne', 'Johnstohn', 'Belb']
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
message = friends[-2] + "," + " " + "thanks for accepting the invite!"
print(message)
#transpo list
cars = ['Lamborghini', 'Toyota Camry', 'Prius', 'Ford Model T']
car_attributes = ['fuel efficiency', 'vintage', 'luxury', 'reliability']
statement = "My favorite car for" + " " + car_attributes[-1] + " " "is a" + " " + cars[-1] + "."
print(statement)
cars.append("Volvo")
print(cars)
car_attributes.append("Safety")
print(statement)
print(car_attributes) 
watches = []
watches.append('rolex')
watches.append('seiko')
watches.append('breitling')
print(watches)
watches.insert(2, "tissot")
print(watches)
popped_watches = watches.pop(1)
print(watches)
print(popped_watches)
statement = "I just sold my" + " "+ (popped_watches.title())+"."
print(statement)
print(watches)
too_expensive = 'breitling'
watches.remove(too_expensive)
print(watches)
print("The" + " " + (too_expensive) + " " + "watch was too costly.")

#Rabbis
Rabbis = ['r moshe feinstein', 'the satmar rov', 'the chazon ish', 'rav Soleveitchik', 'Rav Ovadia Yosef']
for rav in Rabbis:
	print(rav) 
for rav in Rabbis:
	print(rav.title() + " was a great Torah scholar.")
	print("I bentsh you that you should grow to be like " + rav.title() + "!\n")
print("Olam Haboh iz a gutteh zach, lernen Torah iz a bessreh zach! " )
numbers = list(range(1,6))
print(numbers)

#Hello admin
names = ['kjsd', 'quinn', 'quell', 'chuck norris', 'john admin', 'admin', 'john bonham']

if names:
	for name in names:
		if name != 'admin':
			print("Hey, " + name.title() + "! Welcome to the site!")
		elif 'admin' in names:
	 		print('Hey there Admin! Want to see a user report?')
else:
	print("let's get some names on here!")

#User names

current_users = ['bohn', 'bred', 'bourg', 'bapple', 'yehoynesin']
new_users = ['tallit', 'pewter', 'bourg ', 'Yehoynesin', 'jimbo']
for n_u in new_users:
	n_u = n_u.lower()
	n_u = n_u.strip()
	if n_u in current_users:
		print("The user name " + n_u + " is in use.  Please pick a new one.")
	else:
		print('Great name choice!')