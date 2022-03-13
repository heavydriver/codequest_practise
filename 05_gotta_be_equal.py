n = int(input())
w = []

not_possible = True

for x in range(0, n, 1):
    w.append(int(input()))

for x in range(0, n, 1):
    if ((sum(w[:x]) - sum(w[x:])) == 0):
        print("Woohoo let's split it! Put %d trophies on the first freight car." % x)
        not_possible = False
        break;

if(not_possible):
    print("Looks like we're spending extra money on fuel.")

