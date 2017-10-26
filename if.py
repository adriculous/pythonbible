# "if" statements, comparison operators, booleans stuff

num1 = 120
num2 = 120

if num1 > num2:
    print("num1 is bigger than num2")
elif num2 > num1:
    print("num2 is bugger than num1")
else:
    print("both numbers are equal")

# "If this is true, then do this. If it's not, do this instead. (If it's still not true,
# do this, etc. etc.) Otherwise, they're both equal.
# (and let it be known of this fact.)"

# logical operators stuff

A = 19
B = 45

if not A < B:
    print("Well yeah, obviously not true.")


if (A > 10 and B > 10):
    print("Yep, both seem to be true.")


if A > 10 or B < 10:
    print("They're both true.")

if not ((A > 10 and B > 10) or (A > 45 nd B > 45)):
    print("Looks complicated, but true.")
