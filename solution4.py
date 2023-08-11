def num_within(x, min, max):
    if x >= min and x <=max:
        return True
    else:
        return False

print(num_within(3, 2, 4))
print(num_within(3,1,3))
print(num_within(2, 2, 5))
print(num_within(10,2,5))