'''tic-tak-toe'''

n = 3
m = 3
cx = "\033[31m{}\033[0m".format('X')
co = "\033[32m{}\033[0m".format('O')


def generate_empty_field(n, m):
    field = [0] * n
    for i in range(n):
        field[i] = [0] * m
    return field;

def print_field(field):
    print(('- ') * len(field[0]))
    for line in field:
        for elem in line:
            print(elem, end=' ')
        print()
    print(('- ') * len(field[0]))

def get_user_input():
    try:
        x = int(input())
        y = int(input())
        return (x - 1, y - 1)
    except:
        print("Are you sure that it is correct? Try again")
    return (None, None)

def is_input_correct(x, y, field):
    if (x, y) == (None, None):
        return False
    if x >= 0 and x <= n - 1 and y >= 0 and y <= m - 1 and (field[x][y] == 0):
        return True
    return False

def is_win(field, pl):
    if (field[0][0] == field[0][1] == field[0][2] == pl) or \
            (field[0][0] == field[1][0] == field[2][0] == pl) or \
            (field[0][0] == field[1][1] == field[2][2] == pl) or \
            (field[0][0] == field[0][1] == field[0][2] == pl) or \
            (field[0][1] == field[1][1] == field[2][1] == pl) or \
            (field[0][2] == field[1][2] == field[2][2] == pl) or \
            (field[1][0] == field[1][1] == field[1][2] == pl) or \
            (field[2][0] == field[2][1] == field[2][2] == pl):
        return 1
    else:
        return 0

def move_of_player(field, pl):
    print("Input coordinates for "+pl)
    while True:
        x, y = get_user_input()
        if is_input_correct(x, y, field):
            field[x][y] = pl
            print_field(field)
            return
        else:
            print("Incorrect coordinates. Try again")

# def find_empty_pos(field):
#     empty_pos = []
#     for i in range(n):
#         for j in range(m):
#             if field[i][j] == 0:
#                 empty_pos.append((x, y))
#     return empty_pos

def rate_field(field, pl):
    test_field = field
    rating_filed=generate_empty_field(n, m)
    for i in range(n):
        for j in range(n):
            if test_field[i][j] == 0:
                test_field[i][j] = pl
                if is_win(test_field, pl) == 1:
                    rating_filed[i][j] += 1000
                else:
                    rating_filed[i][j] += 0
                test_field[i][j] = 0
    for i in range(n):
        for j in range(m):
            if test_field[i][j] == 0:
                test_field[i][j] = pl
                if is_win(test_field, pl) == 0:
                    for k in range(n):
                        for l in range(m):
                            if test_field[k][l] == 0:
                                test_field[k][l] = pl
                                if is_win(test_field, pl) == 1:
                                    rating_filed[i][j] += 50
                                else:
                                    rating_filed[i][j] += 0
                                test_field[k][l] = 0
                test_field[i][j] = 0
    for i in range(n):
        for j in range(m):
            if test_field[i][j] == 0:
                test_field[i][j] = pl
                if is_win(test_field, pl) == 0:
                    for k in range(n):
                        for l in range(m):
                            if test_field[k][l] == 0:
                                test_field[k][l] = pl
                                if is_win(test_field, pl) == 0:
                                    for s in range(n):
                                        for t in range(m):
                                            if test_field[s][t] == 0:
                                                test_field[s][t] = pl
                                                if is_win(test_field, pl) == 1:
                                                    rating_filed[i][j] += 2
                                                else:
                                                    rating_filed[i][j] += 0
                                                test_field[s][t] = 0
                                test_field[k][l] = 0
                test_field[i][j] = 0
    print("Rating field for "+pl)
    print_field(rating_filed)
    return rating_filed

def find_max_rating(rating_field):
    max = 0
    for i in range(n):
        for j in range(m):
            if rating_field[i][j] > max:
                max = rating_field[i][j]
    return max

def find_coord_of_max_rating(rating_field):
    max_rating = find_max_rating(rating_field)
    for i in range(n):
        for j in range(m):
            if rating_field[i][j] == max_rating:
                return i, j

# def computers_move(field, round):
#     if (round == 1):
#         if (field[1][1] == 0):
#             x, y = 1, 1
#         else:
#             x, y = 0, 0
#     if (round == 2):
#         x, y = is_win_possible(field, cx)
#         if (x, y) == (None, None):
#             if field[1][1] == cx:
#                 x, y = 0, 2
#             else:
#                 x, y = double_is_win_possible(field, cx)
#     if (round >= 3):
#         x, y = is_win_possible(field, co)
#         if (x, y) == (None, None):
#             x, y = is_win_possible(field, cx)
#     field[x][y] = co
#     print_field(field)

def move_of_computer(field):
    rating_field_for_O = rate_field(field, co)
    max_rating_O = find_max_rating(rating_field_for_O)
    rating_field_for_X = rate_field(field, cx)
    max_rating_X = find_max_rating(rating_field_for_X)
    if max_rating_O >= 1000:
        x, y = find_coord_of_max_rating(rating_field_for_O)
    elif max_rating_X >= 1000:
        x, y = find_coord_of_max_rating(rating_field_for_X)
    else:
        x, y = find_coord_of_max_rating(rating_field_for_O)
    field[x][y] = co
    print_field(field)

def play_again():
    print("Do you want to play again?\n Input \"y\" or \"n\":")
    if (input() == "y"):
        return True
    else:
        return False

def playerVSplayer():
    field = generate_empty_field(n, m)
    print_field(field)
    current_player = cx
    while True:
        move_of_player(field, current_player)
        if (is_win(field, cx)):
            print("1st player wins!!!")
            if play_again():
                playerVSplayer()
            else:
                return 1
        if current_player == cx:
            current_player = co
        else:
            current_player = cx

def playerVScomputer():
    field = generate_empty_field(n, m)
    print_field(field)
    while True:
        move_of_player(field, cx)
        if (is_win(field, cx)):
            print("You win!!!")
            if play_again():
                playerVScomputer()
            else:
                return
        move_of_computer(field)
        if (is_win(field, co)):
            print("You lose!!!")
            if play_again():
                playerVScomputer()
            else:
                return

playerVScomputer()