a = (1,2,3,4,5,4,4,4,4)
print(type(a))

# count method 

num = a.count(4)
print(num)


# index method 

num  = a.index(2)
print(num)

# repeated tuple

tuple = (1,2,3)

repeated = tuple * 3
print(repeated)

# concatinated tuple 

tuple1 = (1,2,3)
tuple2 = (4,5,6)

concatinate = tuple1 + tuple2
print(concatinate)

# membership : you can check that wheather it is in the tuple or not
# using (in)  keyword 
my_tuple = ("talha",1,2,3,4,"khanwali")
let = ("talha" in my_tuple)
print(let)

# len ()  method 

tuple = (1,2,3,4,5)
print(len(tuple))