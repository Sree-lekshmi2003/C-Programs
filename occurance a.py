num_names = int(input("Enter the number of names: "))

names = []
for _ in range(num_names):
    name = input("Enter a name: ")
    names.append(name)

count_a = sum(name.lower().count('a') for name in names)

print(f"The total occurrence of 'a' is: {count_a}")
