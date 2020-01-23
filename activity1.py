space1 = "X"
space2 = "X"
space3 = "X"
space4 = "X"
space5 = "X"
space6 = ""
space7 = "O"
space8 = ""
space9 = ""

print("\n \033[1;32;40m  |   |   ")
print(" {} | {} | {}  ".format(space1, space2, space3))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {} |  {} ".format(space4, space5, space6))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print(" {} | {}  | {}  ".format(space7, space8, space9))
print("   |   |   \n")

if (space1 == space2) and (space1 == space3):
    print("You win!")
else:
    print("You lose!")