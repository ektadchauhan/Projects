def string_length(mystring):
    if type(mystring) == int:
        return "length of integer not possible"
    elif type(mystring) == float:
        return "length of float not possible"
    else:
        return len(mystring)

print (string_length(1))

lst="Terribly Tricky"
print (lst[-9:9])

