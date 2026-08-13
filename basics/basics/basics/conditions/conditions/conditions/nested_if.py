age = int(input("Enter your age: "))

if age >= 18:
    citizenship = input("Are you an Indian citizen? (yes/no): ")

    if citizenship.lower() == "yes":
        print("You can apply for voting.")
    else:
        print("Citizenship requirement not satisfied.")
else:
    print("You are under 18.")
