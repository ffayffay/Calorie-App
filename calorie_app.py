import datetime

daily_cal_total = []
recipe_catalog = []


def directory():
	prompt = input('''
Welcome!
Would you like to make a calorie entry or add to recipe catalog?
C/R >
		''')
	if prompt.lower() == 'c':
		get_daily_cal()
	elif prompt.lower() == 'r':
		get_recipe()


def get_recipe():
	global recipe_catalog

	title = input('What is the recipe title?  >')
	title = title.title()
	calories = input('How many calories are in {}?  >'.format(title))

	recipe_catalog.append({title: calories})
	print(recipe_catalog)
	print(title + ':   '+ calories)
	prompt_for_input()


def get_daily_cal():
	global daily_cal_total
	print("How many calories where in your meal?")
	
	try:
		fay_meal_cal = int(input("Fay  >"))
		jer_meal_cal = int(input("Jer  >"))

		meal_cals = (fay_meal_cal, jer_meal_cal)
		daily_cal_total.append(meal_cals)
	except ValueError:
		print('Entry must be a number! Try again.\n')
		get_daily_cal()

	print("Your total is {} calories".format(sum_cals(daily_cal_total)))
	prompt_for_input()


def sum_cals(daily_cal_total):
	total = (0, 0)
	for cal in daily_cal_total:
		total = (total[0] + cal[0], total[1] + cal[1])

	return total


def prompt_for_input():
	another_entry = input('Would you like to make another entry?  Y/N  >')

	if another_entry.lower() == 'y':
		directory()
	else:
		return print('See you later!')


directory()






now = datetime.datetime.now()
print(now)