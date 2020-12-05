# Part 1
# with open("input.txt", "r") as file:
#     seats = file.readlines()
#     highest_seat_id = 0
#     for seat in seats:
#         row = [0, 127]
#         column = [0, 7]
#         for c in seat:
#             if c == 'F':
#                 row[1] = row[0] + ((row[1] - row[0]) // 2)
#             elif c == 'B':
#                 row[0] = row[1] - ((row[1] - row[0]) // 2)
#             elif c == 'R':
#                 column[0] = column[1] - ((column[1] - column[0]) // 2)
#             elif c == 'L':
#                 column[1] = column[0] + ((column[1] - column[0]) // 2)
#         seat_id = row[0] * 8 + column[0]
#         if seat_id > highest_seat_id:
#             highest_seat_id = seat_id
#     print(highest_seat_id)

# Part 2
with open("input.txt", "r") as file:
    free_seats = list(range(0, 128 * 8 - 1))
    seats = file.readlines()
    highest_seat_id = 0
    for seat in seats:
        row = [0, 127]
        column = [0, 7]
        for c in seat:
            if c == 'F':
                row[1] = row[0] + ((row[1] - row[0]) // 2)
            elif c == 'B':
                row[0] = row[1] - ((row[1] - row[0]) // 2)
            elif c == 'R':
                column[0] = column[1] - ((column[1] - column[0]) // 2)
            elif c == 'L':
                column[1] = column[0] + ((column[1] - column[0]) // 2)
        seat_id = row[0] * 8 + column[0]
        free_seats.remove(seat_id)
    for free_seat in free_seats:
        if not free_seat - 1 in free_seats and not free_seat + 1 in free_seats:
            print(free_seat)
