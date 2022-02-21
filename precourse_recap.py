age = input("How old are you? ")
stephanie_age = 27

print("You are " + age + ".")

if int(age) > stephanie_age:
    age_difference = int(age) - stephanie_age
    print("You are " + str(age_difference) + " year(s) older than Stephanie.")

if int(age) < stephanie_age:
    age_difference = stephanie_age - int(age)
    print("You are " + str(age_difference) + " year(s) younger than Stephanie.")

if int(age) == stephanie_age:
    print("You are the same age as Stephanie.")