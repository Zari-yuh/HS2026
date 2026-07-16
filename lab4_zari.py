# Zari | lab 4 | Intro to python

# Ticket 1 | 
ages = [17, 11, 25, 13, 9]
for age in ages:
    #PREDICT : 11, 9 will get too young, 17, 25, 13 will get access granted
    #it holds the ages
    if age >= 13:
        print ("Access granted")
    else:
        print("Too young")

# Ticket 2 |
keep_checking = "yes"

while keep_checking == "yes":
    keep_checking = input("Do you want to keep checking?")
    if keep_checking :
        print("Access granted")
    else:
        print("Access denied, must be 13 or older.")
    keep_checking = input("Do you want to keep checking? (yes/no)").lower()
    print("Thank you for checking. Goodbye!")

    # Q1 - Yes, but I think only once
    # Q2 - You dont know how many times a user would check an age.

# Ticket 3 |
while True:
    user_input = input("Enter a age or type 'stop': ")
    if user_input.lower() == 'stop':
        print("Goodbye!")
        break
    age = int(user_input)
    if age >= 13:
        print("Access granted")
    else:
        print("Access denied, must be 13 or older.")
    
    # Q1 - The loop wont end
    # Q2 - T2 ends when condition is no longer true, this one relies on break ?

# Ticket 4 |
def can_access(age):
    if age >= 13:
        return True
    else:
        return False


ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(age, "— Access granted ✅")
    else:
        print(age, "— Too young ❌")
# Q1 - This function checks if the age is 13 or older and returns True or False accordingly.
# Q2 - Its more organized.

# Ticket 5 |
def can_access(age):
    return age >= 13

def signup_report(ages):
    approved = 0

    print("--- StreamPass Signup Report ---")

    for number, age in enumerate(ages, start=1):
        if can_access(age):
            print(f"Signup #{number} | Age {age} — Access granted ✅")
            approved += 1
        else:
            print(f"Signup #{number} | Age {age} — Too young ❌")

    print(f"Approved: {approved} out of {len(ages)}")

    signups = [22, 10, 15, 8, 19, 13]
    signup_report(signups)

# Q1 - 22, 15, 19, 13 will get access granted, 10 and 8 will get too young. (4/6)
# Q2 - 