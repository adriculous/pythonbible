# playing around with loopy loops - count from 1 to 10

L = []

while len(L) <3:
    new_name = input("Please add a new name: ").strip().capitalize()
    L.append(new_name)

print("Sorry, list is full.")
print(L)
    
