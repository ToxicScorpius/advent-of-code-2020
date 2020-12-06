from day5_function import find_id, find_my_seat

highest_ID = 0
taken_seats = []
possible_seats = list(range(0, 1024))  # Possible IDs from 0 to 1023
with open("day5_input.txt") as file:
    lines = [line.strip() for line in file]
    for line in lines:
        taken_seats.append(find_id(line))  # Adds the seat's ID number to a list

missing_seats = list(set(possible_seats).difference(taken_seats))  # Compare
my_seat = find_my_seat(missing_seats)

print(my_seat)  # Show differences
