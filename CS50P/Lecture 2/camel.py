input = input("camelCase: ")

for s in input:
    if s.isupper():
        input = input[:input.find(s)] + "_" + input[input.find(s):]
print("snake_case:", input.lower())
