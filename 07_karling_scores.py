import math

first_line = input()
num_of_rounds = int(first_line.split(" ")[0])
karl_score = int(first_line.split(" ")[1])
radius = float(first_line.split(" ")[2])
center = input().split(" ")
locations = []

for x in range(0, num_of_rounds, 1):
    locations.append(input().split(" "))

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow((x2-x1), 2)+math.pow((y2-y1), 2))

distance = []

for location in locations:
    distance.append([calculate_distance(int(center[0]), int(center[1]), int(location[0]), int(location[1])), calculate_distance(int(center[0]), int(center[1]), int(location[2]), int(location[3]))])

score_1 = 0
score_2 = 0

for x in range(0, num_of_rounds, 1):
    if (distance[x][0] <= radius or distance[x][1] <= radius):
        if (distance[x][0] < distance[x][1]):
            score_1 = score_1 + 1
        elif (distance[x][1] < distance[x][0]):
            score_2 = score_2 + 1

if (score_1 >= score_2):
    if (score_1 == karl_score):
        print("YAY KARL U GOT IT!")
    else:
        print("Karl...get some practice")
else:
    if (score_2 == karl_score):
        print("YAY KARL U GOT IT!")
    else:
        print("Karl...get some practice")