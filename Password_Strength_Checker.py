pw = input("Enter a password: ")

if len(pw) < 9:
    print("Weak")
else:
    print("Strong")