def traverse_map(map, x_step, y_step):
    x = 0
    y = 0
    num_trees = 0
    while y < len(map):
        if map[y][x] == '#':
            num_trees += 1
        x = (x + x_step) % (len(map[0]) - 1)
        y = y + y_step
    return num_trees


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        lines = file.readlines()
        print(traverse_map(lines, 3, 1))
        result = traverse_map(lines, 1, 1) * traverse_map(lines, 3, 1) * traverse_map(lines, 5, 1) * traverse_map(lines, 7, 1) * traverse_map(lines, 1, 2)
        print(result)

