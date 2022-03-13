from datetime import timedelta

n = int(input())
times = []

for x in range(0, n, 1):
    times.append([input(), input().split(" ")])

delays = []

for time in times:
    t1 = timedelta(hours=int(time[1][0].split(":")[0]), minutes=int(time[1][0].split(":")[1]))
    t2 = timedelta(hours=int(time[1][1].split(":")[0]), minutes=int(time[1][1].split(":")[1]))
    delays.append(t2-t1)

output_str = []

for x in range(0, n, 1):
    output_str.append(times[x][0]+" was")
    if (delays[x].seconds / 3600 == 1):
        output_str.append(str(int(delays[x].seconds / 3600))+" hour")
    elif (delays[x].seconds / 3600 > 1):
        output_str.append(str(int(delays[x].seconds / 3600))+" hours")

    if ((delays[x].seconds % 3600) // 60 == 1):
        if (len(output_str) == 2):
            output_str.append("and")
        output_str.append(str((int(delays[x].seconds % 3600) // 60))+" minute")
    elif((delays[x].seconds % 3600) // 60 > 1):
        if (len(output_str) == 2):
            output_str.append("and")
        output_str.append(str((int(delays[x].seconds % 3600) // 60))+" minutes")
    
    if (len(output_str) == 1):
        output_str.append("on time.")
    else:
        output_str.append("late.")
    
    print(" ".join(output_str))
    output_str = []