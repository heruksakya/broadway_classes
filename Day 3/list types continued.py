a = [(4, 12, 5), (6, 1), (11, 12), (6, 7, 8)]

def sort_based_on_last(data):
    return data[-1]

a.sort(key = sort_based_on_last)
print(a)

a = ["Hello", "from", "Broadway"]
a.reverse()
print(a)

