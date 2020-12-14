# Part 1

# directions = ['EAST', 'SOUTH', 'WEST', 'NORTH']
#
# with open('input.txt', 'r') as file:
#     instructions = file.read().split('\n')
#     west_east = 0
#     north_south = 0
#     current_direction = 0
#     for i in instructions:
#         action = i[0]
#         val = int(i[1:])
#         if action == 'N' or (action == 'F' and directions[current_direction] == 'NORTH'):
#             north_south += val
#         elif action == 'E' or (action == 'F' and directions[current_direction] == 'EAST'):
#             west_east += val
#         elif action == 'S' or (action == 'F' and directions[current_direction] == 'SOUTH'):
#             north_south -= val
#         elif action == 'W' or (action == 'F' and directions[current_direction] == 'WEST'):
#             west_east -= val
#         elif action == 'L':
#             current_direction = (current_direction - (val // 90)) % 4
#         elif action == 'R':
#             current_direction = (current_direction + (val // 90)) % 4
#     print((abs(west_east) - 0) + (abs(north_south) - 0))

# Part 2

with open('input.txt', 'r') as file:
    instructions = file.read().split('\n')
    ship_WE = 0
    ship_NS = 0
    waypoint_WE = 10
    waypoint_NS = 1
    for i in instructions:
        action = i[0]
        val = int(i[1:])
        if action == 'N':
            waypoint_NS += val
        elif action == 'E':
            waypoint_WE += val
        elif action == 'S':
            waypoint_NS -= val
        elif action == 'W':
            waypoint_WE -= val
        elif action == 'F':
            ship_NS += val * waypoint_NS
            ship_WE += val * waypoint_WE
        elif action == 'R':
            for j in range(val // 90):
                waypoint_NS, waypoint_WE = -waypoint_WE, waypoint_NS
        elif action == 'L':
            for j in range(val // 90):
                waypoint_NS, waypoint_WE = waypoint_WE, -waypoint_NS
    print(abs(ship_NS) + abs(ship_WE))
