file = open("/etc/passwd", "r")
data = file.read()
file.close()

username = input("Enter a linux user account name: ")

if username in data:
    print("Found User!")

lines = data.split("\n")

for line in lines:
    fields = line.split(":")
    if username == fields[0]:
        print("User found!")
        print(fields[5])
        exit(0)

print("Error, user not found. Could not locate " + username + " on the system. Exiting.")
exit(1)

