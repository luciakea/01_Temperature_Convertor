# Display output using int()


to_round = [1/1, 1/2, 1/3]
print("**** Numbers to round *****")
print(to_round)

print()
print("**** Rounded Numbers ****")

for item in to_round:
    try:
        integer= int(item)
        print(integer)
    except ValueError:
        print("{:.1f}".format(item))