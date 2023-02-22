def main():
    tictac = "         "
    print("---------")
    print("|", tictac[0], tictac[1], tictac[2], "|")
    print("|", tictac[3], tictac[4], tictac[5], "|")
    print("|", tictac[6], tictac[7], tictac[8], "|")
    print("---------")
    tictac_dict = {
        "1 1": tictac[0], "1 2": tictac[1], "1 3": tictac[2],
        "2 1": tictac[3], "2 2": tictac[4], "2 3": tictac[5],
        "3 1": tictac[6], "3 2": tictac[7], "3 3": tictac[8]
    }
    player_x = True
    while True:
        move = input()
        move_int = move.split()

        if not is_number(move_int):
            print("You should enter numbers!")
            continue

        if not is_valid_number(move_int):
            print("Coordinates should be from 1 to 3!")
            continue

        if is_cell_not_empty(tictac_dict, move):
            print("This cell is occupied! Choose another one!")
            continue

        take_move(move, tictac_dict, player_x)
        player_x = not player_x
        res, finished = is_game_finished(tictac_dict)
        if finished:
            print(res)
            break


def is_number(move_int):
    if move_int[0].isdigit() is False and move_int[1].isdigit() is False:
        return False
    return True


def is_valid_number(move_int):
    if int(move_int[0]) >= 4 or int(move_int[1]) >= 4 or int(move_int[0]) < 1 or int(move_int[1]) < 1:
        return False
    return True


def is_cell_not_empty(tictac_dict, move):
    if tictac_dict[move] == "X" or tictac_dict[move] == "O":
        return True
    return False


def take_move(move, tictac_dict, player_x):
    tictac_dict[move] = "O"
    if player_x:
        tictac_dict[move] = "X"
    print("---------")
    print("|", tictac_dict["1 1"], tictac_dict["1 2"], tictac_dict["1 3"], "|")
    print("|", tictac_dict["2 1"], tictac_dict["2 2"], tictac_dict["2 3"], "|")
    print("|", tictac_dict["3 1"], tictac_dict["3 2"], tictac_dict["3 3"], "|")
    print("---------")


def is_game_finished(tictac_dict):
    empty_list = 0
    x_list = []
    o_list = []
    for i in tictac_dict:
        if tictac_dict[i] == "X":
            x_list.append(i)
        if tictac_dict[i] == "O":
            o_list.append(i)
        if tictac_dict[i] == " ":
            empty_list += 1
    win_combinations = [["1 1", "1 2", "1 3"], ["2 1", "2 2", "2 3"], ["3 1", "3 2", "3 3"], ["1 1", "2 1", "3 1"], ["1 2", "2 2", "3 2"], ["1 3", "2 3", "3 3"], ["1 1", "2 2", "3 3"], ["1 3", "2 2", "3 1"]]
    if is_x_win(x_list, win_combinations):
        return "X wins", True
    if is_o_win(o_list, win_combinations):
        return "O wins", True
    if is_draw(empty_list):
        return "Draw", True
    return "", False


def is_impossible(x_list, o_list, win_combinations):
    diff = len(x_list) - len(o_list)
    absolute_value = abs(diff)
    if absolute_value >= 2:
        return True
    x_win = False
    o_win = False
    for i in win_combinations:
        if sorted(set(i).intersection(x_list)) in win_combinations:
            x_win = True
        if sorted(set(i).intersection(o_list)) in win_combinations:
            o_win = True
    return x_win and o_win


def is_draw(empty_list):
    if empty_list == 0:
        return True
    return False


def is_x_win(x_list, win_combinations):
    for i in win_combinations:
        if sorted(set(i).intersection(x_list)) in win_combinations:
            return True
    return False


def is_o_win(o_list, win_combinations):
    for i in win_combinations:
        if sorted(set(i).intersection(o_list)) in win_combinations:
            return True
    return False


main()
