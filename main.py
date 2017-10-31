


m, n = map(int, tuple(input().split()))

friends = []
for i in range(m*n):
    temp = list(map(int, input().split()))[2:]
    friends.append(temp)

placed = [0 for _ in range(m*n)]

class_room = [[-1 for i in range(n)] for j in range(m)]


def is_safe(place, student):

    row, col = place

    for i in range(m):
        for j in range(n):
            in_fight_position = (i,j) != place and j != col and i != row and i-j == row - col and i+j == row + col
            if (in_fight_position and class_room[row][col] not in friends[student]):
                return False
    return True


def arrange_backtrack(place):

    for i in range(m*n):
        row = i // n
        col = i % m

        if placed[i] != 1 and is_safe((row,col),i):

           # print(class_room)

            if place == m*n -1:
                for i in range(m):
                    print(class_room[i])
                return


            class_room[row][col] = i
            arrange_backtrack(place + 1)

    class_room[row][col] = -1








