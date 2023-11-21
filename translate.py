

file = open("rig.txt", "r")
filedata = file.read()
file.close()

string_ids = filedata.split("\n\n")

def rig_to_dict(rig):
    person = {}
    li = rig.split("\n")
    names = li[0].split(" ")
    person["first"] = names[0]
    person["last"] = names[1]
    person["address"] = li[1]
    line3_split = li[2].split(" ")
    city_state = line3_split[0]
    person["zip"] = line3_split[1]
    city_state = city_state.split(", ")
    person["city"] = city_state[0]
    person["state"] = city_state[1]
    person["phone"] = li[3]
    return person

def dict_to_rec(person):
    record = [
        person["first"],
        person["last"],
        person["address"],
        person["city"],
        person["state"],
        person["zip"],
        person["phone"],
    ]
    return ",".join(record)

people = []
for str_id in string_ids:
    person = rig_to_dict(str_id)
    people.append(person)

# To CSV format
records = []
for p in people:
    records.append(dict_to_rec(p))


filedata = "\n".join(records)
file = open("identities.csv", "w")
file.write(filedata)
file.close()
