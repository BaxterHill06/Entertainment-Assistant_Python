file = open("Genre.CSV", "r")

for line in file:
    arr = line
arr = arr.split(",")

arr.sort()
print(" ".join(arr).strip("'").strip(" ").strip("\n").replace(" ", ","))
print("0," * len(arr))

