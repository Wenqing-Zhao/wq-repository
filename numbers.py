#
num = int(input("Enter a number:"))
print("\t Times", num, "Table")
print("————————————————————————")
i = 0
while i <= num:
    if i == 0:
        print("|", i, "\t|\t\t", i * num, "\t\t|")
    else:
        print("|", i, "\t|\t\t", i * num, "\t|")
    i += 1
print("————————————————————————")
