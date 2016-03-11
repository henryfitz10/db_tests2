# without mapping
items = [1, 2, 3, 4, 5]

squared = []
for x in items:
    squared.append(x ** 2)
print squared


# with mapping

items = [1, 2, 3, 4, 5]


def sqr_even(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return 0


result = map(sqr_even, items)

print result

# with filter
evens = filter(lambda a: a != 0, result)

print evens



