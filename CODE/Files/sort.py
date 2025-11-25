file = open("Genre.CSV", "r")

for line in file:
    arr = line
arr = arr.split(",")

arr.sort()
print(arr)
print("0," * len(arr))

