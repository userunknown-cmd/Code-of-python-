marks = {
    "talha" : 60,
    "wali" : 34,
    "khan" : 80,
    0 : "harry"  #yes you can use the interger and the strings as key and value pair
}

# .items() method

print(marks.items(), type(marks))

# key() method
# return the keys 
print(marks.keys())

# get() method 
# return the values of the keys 
print(marks.get("wali"))
# note
print(marks.get("wali")) # it will prints non if we chnage the wali to wali1
print(marks["wali"]) # it will retrun an error ( so both are different)


# the marks are updated and the dictionary is changed coz it is mutable 
# update() method is used 
marks.update({"wali":90 , "talhan": 99})
print(marks)
