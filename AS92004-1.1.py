# First name and age
first_name =input("What is you full name?")
age = int(input("How old are you?"))
#if age is between 5 and 17 you can do it but if younger or older then that you are too older or young to do it
if age < 5:
    print("Sorry you are to young to join the camp")
if age > 17:
    print("Sorry you are to old to join the camp")

# Choosing a activity to do
chosen_activity = ["Cultural Immersion (5 days, easy, $800 fee)","Kayaking and Pancake (3 days, moderate, $400 fee)", "Mountain biking (4 Days, difficult, $900 fee)"]
print("Choose an activity")
print(f"1. {chosen_activity[0]}")
print(f"2. {chosen_activity[1]}")
print(f"3. {chosen_activity[2]}")
chosen_activity = int(input("Enter the number of your chosen activity:")) - 1
print("Choose one of the activity to do:")
if chosen_activity == 1:
    total_fee = 800
elif chosen_activity == 2:
    total_fee = 400
elif chosen_activity == 3:
    total_fee = 900

if chosen_activity == 1:
    name_of_activity = (f"{chosen_activity[0]}")
elif chosen_activity == 2:
    name_of_activity = (f"{chosen_activity[1]}")
elif chosen_activity == 3:
    name_of_activity = (f"{chosen_activity[2]}")

#choosing Meal options 
meal_options = ["Standard", "Vegetarian", "Vegan"]
print("Choose a Meal")
print(f"1. {meal_options[0]}")
print(f"2. {meal_options[1]}")
print(f"3. {meal_options[2]}")
print(f"4. {meal_options[3]}")
meal_option = int(input("Enter the number of your choice meal"))

if meal_option == 1:
    name_of_meal = (f"{meal_option[0]}")
elif chosen_activity == 2:
    name_of_meal = (f"{meal_option[1]}")
elif chosen_activity == 3:
    name_of_meal = (f"{meal_option[2]}")