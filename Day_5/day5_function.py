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

    id_num = min_row * 8 + min_column
    if id_num is not None:
        return id_num  # Return the ID number
    return None


def find_my_seat(seats_list):
    """Find the isolated seat's ID."""
    n = 0
    for index in seats_list[:-1]:  # Prevents index errors
        # If the previous and next values arent part of the sequence (n-1, n, n+1)
        if index + 1 != seats_list[n + 1] and index - 1 != seats_list[n - 1]:
            return index  # This is my seat !
        n += 1
    return None
