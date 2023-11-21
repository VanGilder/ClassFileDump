#Dictionary
data = {
    "first": "Brayden",
    "last": "VanGilder",
    "email": "bvangilder1@sycamores.indstate.edu",
    "account": "cs33134",
    "month": 9,
    "day": 20
}

#string pad method to add the 0
monthNum = str(data["month"]).rjust(2, "0")

#Concatenation message
msg = "My name is " + data["first"].title() + " " + data["last"].title() + ", my email address is " + data["email"] + ", my CS Server account is " + data["account"] + ", and my birthday is " + monthNum + "-" + str(data["day"])

#Interpolation message
msg2 = f'My name is {data["first"].title()} {data["last"].title()}, my email address is {data["email"]}, my CS Server account is {data["account"]}, and my birthday is {str(data["month"]).rjust(2, "0")}-{data["day"]}'

print(msg)
print(msg2)

#example output My name is Brayden VanGilder, my email address is bvangilder1@sycamores.indstate.edu, my CS Server account is cs33134, and my birthday is 09-20.
