def menu_is_boring(meals):
    for i in range(len(meals) - 2):
        if meals[i] == meals[i + 1]:
            return True
    return False
meals_1=['Readneck Ribs', 'Prawn Star', 'San Quentin Squid', 'Fist Full of Pizza', 'Honky Tonk Chicken']
meals_2=['Readneck Ribs', 'Prawn Star', 'Running Bear Salmon', 'Running Bear Salmon', 'Honky Tonk Chicken']
print( menu_is_boring(meals_1))
print( menu_is_boring(meals_2))

