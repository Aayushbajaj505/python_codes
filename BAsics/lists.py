m = list(range(20))  # list from 1 to 20
print(m)
n = list("Hello world")  # list of all the letters
print(n)
# unpacking lists
d = [1, 2, 3]
one, two, three = d
# in this method both sides should have equal variables
# but if we want only first two then we can unpack the rest  like this
four, five, *other = m
# if we want only first and last item
first, *other1, last = m
print(last)
print(other1)
# enumerate function- gives an index and value tupple
for x in enumerate(m):
    print(x)
