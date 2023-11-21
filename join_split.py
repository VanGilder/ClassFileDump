li = ["cat", "dog", "bird"]

def join(delimiter, li):
    if len(li) == 0:
        return
    s = li[0]
    for item in li[1:]:
        s+= delimiter + item
    return s

print ("_".join(li))
print("_".join(["cat"]))
print("_".join([]))
print("---------------------")
print(join("_", li))
print(join("_", ["cat"]))
print(join("_",[]))
print("========================")


def split(s, delimiter):
    li = []
    last_match = 0
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == delimiter:
            li.append(s[last_match:i])
            last_match = i+1
        i+= 1
    li.append(s[last_match:])
    return li


s = join("_", li)
print(s)
print(s.split("_"))
print("cat".split("_"))
print("".split("_"))
print("-----------------------")
print(split(s, "_"))
print(split("cage", "_"))
print(split("", "_"))
