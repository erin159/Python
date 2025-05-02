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
    name_of_activity = "Cultural Immersion (5 days, easy, $800 fee)"
elif chosen_activity == 2:
    name_of_activity = "Kayaking and Pancake (3 days, moderate, $400 fee)"
elif chosen_activity == 3:
    name_of_activity = "Mountain biking (4 Days, difficult, $900 fee)"


#choosing Meal options 
meal_options = ["Standard", "Vegetarian", "Vegan"]
print("Choose a Meal")
print(f"1. {meal_options[0]}")
print(f"2. {meal_options[1]}")
print(f"3. {meal_options[2]}")
meal_option = int(input("Enter the number of your choice meal"))

if meal_options == 1:
    name_of_meal = "Standard"
elif chosen_activity == 2:
    name_of_meal = "Vegetarian"
elif chosen_activity == 3:
    name_of_meal = "Vegan"

# Asking if you need a shuttle bus to get to the camp 
while True:
    final_question = input(f"Do you need a shuttle bus to get to the camp?")
    final_question = input(f"for the shuttle bus it is an extra $80, are you ok with that?")
    final_question = final_question.lower ()
    if final_question == "yes" or final_question == "no" :
        break
    else:
        print("Please enter yes or no")
if final_question == "yes":
    total_fee = 80
elif final_question == "no":
    total_fee = 0

print(f"your name is {first_name}, you are {age} years old, the activity you choose was {chosen_activity}, your meal option you choose was  {meal_option}. the total cost is ${total_fee + total_fee}")
while True:
    final_decision = input(f"Do you want to proceed with the payment of the ${total_fee} (yes/no): ")
    if len(final_decision) == 0:
        print("Invalid input. Please enter yes or no")
    elif final_decision.lower() in ['yes' , 'y']:
        print("Payment accepted. Thank you!")
        exit()
    elif final_decision.lower() in ['no' , 'n']:
        print("Payment cancelled.")
        exit()
    elif:
        print("invalid input. Please enter 'yes' or 'no'.")