inputs = []
while True:
    inp = input()
    if inp == "":
        break
    inputs.append(inp)

d = {s.split(' ')[1] : int(s.split(' ')[0]) for s in inputs}

print(max(d, key=d.get))