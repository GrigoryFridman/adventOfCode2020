def find_visible_seats(r, s, all_seats):
    vis_seats = []
    for seat_up in range(r - 1, -1, -1):
        if all_seats[seat_up][s] != '.':
            vis_seats.append(all_seats[seat_up][s])
            break
    for seat_down in range(r + 1, len(all_seats)):
        try:
            if all_seats[seat_down][s] != '.':
                vis_seats.append(all_seats[seat_down][s])
                break
        except IndexError:
            print(r, s, seat_down)
    for seat_left in range(s - 1, -1, -1):
        if all_seats[r][seat_left] != '.':
            vis_seats.append(all_seats[r][seat_left])
            break
    for seat_right in range(s + 1, len(all_seats[0])):
        if all_seats[r][seat_right] != '.':
            vis_seats.append(all_seats[r][seat_right])
            break
    for d1_seat_left, d1_seat_up in zip(range(s - 1, -1, -1), range(r - 1, -1, -1)):
        if all_seats[d1_seat_up][d1_seat_left] != '.':
            vis_seats.append(all_seats[d1_seat_up][d1_seat_left])
            break
    for d1_seat_right, d1_seat_down in zip(range(s + 1, len(all_seats[0])), range(r + 1, len(all_seats))):
        if all_seats[d1_seat_down][d1_seat_right] != '.':
            vis_seats.append(all_seats[d1_seat_down][d1_seat_right])
            break
    for d2_seat_left, d2_seat_down in zip(range(s - 1, -1, -1), range(r + 1, len(all_seats))):
        if all_seats[d2_seat_down][d2_seat_left] != '.':
            vis_seats.append(all_seats[d2_seat_down][d2_seat_left])
            break
    for d2_seat_right, d2_seat_up in zip(range(s + 1, len(all_seats[0])), range(r - 1, -1, -1)):
        if all_seats[d2_seat_up][d2_seat_right] != '.':
            vis_seats.append(all_seats[d2_seat_up][d2_seat_right])
            break
    return vis_seats


with open('input.txt', 'r') as file:
    rows = file.read().split('\n')
    num_rows = len(rows)
    width_row = len(rows[0])

    num_changes = 1
    while num_changes > 0:
        seats_to_change = []
        num_changes = 0
        for i, row in enumerate(rows):
            for j, seat in enumerate(row):
                if seat == '.':
                    continue
                visible_seats = find_visible_seats(i, j, rows)
                occ_adj_seats = visible_seats.count('#')
                # print(i, j, visible_seats, sep=', ')
                if (seat == '#' and occ_adj_seats >= 5) or (seat == 'L' and occ_adj_seats == 0):
                    seats_to_change.append((i, j))
        num_changes = len(seats_to_change)
        for change in seats_to_change:
            if rows[change[0]][change[1]] == '#':
                rows[change[0]] = rows[change[0]][:change[1]] + 'L' + rows[change[0]][change[1] + 1:]
            elif rows[change[0]][change[1]] == 'L':
                rows[change[0]] = rows[change[0]][:change[1]] + '#' + rows[change[0]][change[1] + 1:]

    print(sum(r.count('#') for r in rows))
