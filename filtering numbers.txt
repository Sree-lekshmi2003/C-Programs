
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))

filtered_list = ["over" if num > 100 else num for num in numbers]

print("Filtered list:", filtered_list)