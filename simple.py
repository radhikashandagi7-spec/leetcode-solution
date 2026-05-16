agent = [0, 0]
goal = [4, 3]

while agent != goal:
    print("agent at:", agent)

    if agent[0] < goal[0]:
        agent[0] += 1
    elif agent[0] > goal[0]:
        agent[0] -= 1
    elif agent[1] < goal[1]:
        agent[1] += 1
    elif agent[1] > goal[1]:
        agent[1] -= 1

print("agent reached goal", agent)