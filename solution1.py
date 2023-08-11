def max_num(x, y, z):
    largest = x
    if y > largest:
        largest = y
    if z > largest:
        largest = z
    print(largest)

max_num(6,3,1)