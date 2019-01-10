# stars assignment #3

# print output below
# with one for loop
# and distributed spaces
# so it looks like an hour glass

# ******
#  ****
#   **
#   
#   **
#  ****
# ******

for counter in range(-3, 4, 1):
    num_spaces = abs(abs(counter) - 3)
    #print(num_spaces)
    print((" " * num_spaces) + ("*" * abs(counter) * 2))
