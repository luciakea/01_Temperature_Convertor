# quick component to convert degrees F to C
# function takes in value, does conversion and puts answer into a list

def to_c(from_f):
    celsius = (from_f - 32) * 5 / 9
    return celsius


# main routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees F is {} C".format(item, answer)
    converted.append(ans_statement)

for x in range(len(converted)):
    print(converted[x])
