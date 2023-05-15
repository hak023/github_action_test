nPiramidLine = 10
def print_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * (2 * i + 1))

rows = int(nPiramidLine)
print_pyramid(rows)
print("piramid line: {}".format(nPiramidLine))


exit(True)