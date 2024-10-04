try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ZeroDivisionError
    if age >= 18:
        print("You are eligible.")
except ZeroDivisionError:
    print("You are too young for this site.")
except ValueError:
    print("Invalid input.")
except Exception:
    print("Erorr detected")