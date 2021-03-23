game_over = False
grid_map = [
    (1, 1), (1, 2), (1, 3),
    (2, 1), (2, 2), (2, 3),
    (3, 1), (3, 2), (3, 3)
]


# Get the initial game state from the user
def ask_for_game_cells():
    return list(input("Enter cells: "))


# Printing the game in a grid format
def print_game_grid(game_string):
    temp = 0
    print("---------")
    for i in range(0, 3):
        print("|", end=" ")
        for j in range(3):
            j += temp
            if game_string == "":
                print(" ", sep=" ", end=" ")
            else:
                print(game_string[j], sep=" ", end=" ")
        temp = j + 1
        print("|")
    print("---------")


# Analyzing the game state and proclaim the winner
def analyze_game_state(game_matrix):
    global game_over
    three_in_row = (game_matrix[0:3], game_matrix[3:6], game_matrix[6:9],
                    game_matrix[0::3], game_matrix[1::3], game_matrix[2::3],
                    game_matrix[0:9:4], game_matrix[2:7:2])
    x_3 = max(row.count("X") for row in three_in_row)
    o_3 = max(row.count("O") for row in three_in_row)

    if (x_3 == o_3 == 3) or abs(game_matrix.count("X") - game_matrix.count("O")) >= 2:
        print("Impossible")
        game_over = True
    elif x_3 == 3:
        print("X wins")
        game_over = True
    elif o_3 == 3:
        print("O wins")
        game_over = True
    elif all([cell != " " for cell in game_matrix]) and (x_3 != 3 and o_3 != 3):
        print("Draw")
        game_over = True
    else:
        pass


# Ask for coordinates in the correct format
def ask_coordinates():
    xy_are_not_correct = True
    while xy_are_not_correct:
        x_, y_ = input("Enter the coordinates: ").split()
        if not (x_.isnumeric() and y_.isnumeric()):
            print("You should enter numbers!")
        else:
            x_ = int(x_)
            y_ = int(y_)
            if not (x_ in range(1, 4)) or not (y_ in range(1, 4)):
                print("Coordinates should be from 1 to 3")
            else:
                return x_, y_


# Fill the chosen grid cell
def fill_cell_grid(x_coordinate, y_coordinate, game_matrix, plyr_one):
    while game_matrix[grid_map.index((x_coordinate, y_coordinate))] != " ":
        print("This cell is occupied! Choose another one!")
        x_coordinate, y_coordinate = ask_coordinates()
    if plyr_one:
        game_matrix[grid_map.index((x_coordinate, y_coordinate))] = "X"
    else:
        game_matrix[grid_map.index((x_coordinate, y_coordinate))] = "O"
    return game_matrix


if __name__ == "__main__":
    game_cells = [" " for i in range(9)]
    print_game_grid(game_cells)
    player_one = True
    while not game_over:
        x, y = ask_coordinates()
        game_cells = fill_cell_grid(x, y, game_cells, player_one)
        player_one = not player_one
        print_game_grid(game_cells)
        analyze_game_state(game_cells)
