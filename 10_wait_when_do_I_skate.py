names = []

names = input().lower().split(", ")

surnames = []

for name in names:
    surnames.append(name.split(" ")[1])

surnames.sort()

surnames = list(dict.fromkeys(surnames))

if ("chen" in surnames):
    surnames.remove("chen")
    surnames.append("chen")

print(" ".join(surnames).title())