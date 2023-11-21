#list
data = [
    "Brayden",
    "VanGilder",
    "bvangilder1@sycamores.indstate.edu",
    "cs33134",
    9,
    20
]

#string pad method to add the 0
monthNum = str(data[4]).rjust(2, "0")

#Concatenation Message
msg = "My name is " + data[0].title() + " " + data[1].title() + ", my email address is " + data[2] + ", my CS Server account is " + data[3] + " and my birthday is " + monthNum + "-" + str(data[5])


#Interpolation Message
msg2 = f"My name is {data[0].title()} {data[1].title()}, my email address is {data[2]}, my CS Server account is {data[3]} and my birthday is {str(data[4]).rjust(2, '0')}-{data[5]}"

print(msg)
print(msg2)

#example output My name is Brayden VanGilder, my email address is bvangilder1@sycamores.indstate.edu, my CS Server account is cs33134, and my birthday is 09-20.

