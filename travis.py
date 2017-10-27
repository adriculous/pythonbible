# list of known users here

known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
    print("Hi! My name is Travis.")
    name = input("What is your name?: ").strip().capitalize()

    if name in known_users:
        print("Name recognized")
    else:
        print("Name NOT recognized")
