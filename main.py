


m, n = map(int, tuple(input().split()))

friends = []
for i in range(m*n):
    temp = list(map(int, input().split()))[2:]
    friends.append(temp)

placed = [0 for _ in range(m*n)]

class_room = [[-1 for i in range(n)] for j in range(m)]


def is_safe(place, student):

    print(place)
    row, col = place

    for i in range(m):
        for j in range(n):
            
            is_not_empty = class_room[row][col] != -1
            in_fight_position = (i,j) != place and j != col and i != row and i-j == row - col and i+j == row + col
            if (is_not_empty and in_fight_position and class_room[row][col] not in friends[student]):
                print("False")
                return False
    return True


def arrange_backtrack(place):
        print(place)
        row = place // n
        col = place % n

        for i in range(m*n):
            if placed[i] != 1 and is_safe((row,col),i):



                if place == m*n -1:
                    class_room[row][col] = i
                    for i in range(m):
                      print(class_room[i])

                    return True

                class_room[row][col] = i
                placed[i] = 1
                print(placed)
                print(class_room)


                found = arrange_backtrack(place + 1)
                if found :
                    return True

                placed[i] = 0


        class_room[row][col] = -1





arrange_backtrack(0)


