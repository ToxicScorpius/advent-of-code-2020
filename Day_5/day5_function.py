def find_id(line):
    """Find the row and column of the seat using the input code."""
    min_row, min_column = 0, 0
    max_row, max_column = 128, 8
    for char in line:
        if char == "F":  # Take lower half
            max_row -= (max_row - min_row) // 2
        if char == "B":  # Take higher half
            min_row += (max_row - min_row) // 2

        if char == "R":  # Take higher half
            min_column += (max_column - min_column) // 2
        if char == "L":  # Take lower half
            max_column -= (max_column - min_column) // 2

    seat_id = min_row * 8 + min_column  # Calculate the ID number
    return seat_id


def find_my_seat(seats_list):
    n = 0
    for index in seats_list:
        if n < len(seats_list) - 1:  # Prevents index errors
            if index + 1 != seats_list[n + 1] and index - 1 != seats_list[n - 1]:
                return index
        n += 1
