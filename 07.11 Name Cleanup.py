def ProperCase(s):
    uppercase = s[0].upper() + s[1:].lower()
    return uppercase
def RemoveNewLine(s):
    return s.replace("\n","")
def Trim(s):
    return RemoveNewLine(s.strip())
def FirstName(s):
    s = s.lstrip()
    firstspace = s.find(" ")
    return Trim(ProperCase(s[0:firstspace]))
def LastName(s):
    s = s.rstrip()
    lastspace = s.rfind(" ")
    return Trim(ProperCase(s[lastspace + 1:]))
def MiddleName(s):
    s = s.lstrip()
    firstspace = s.find(" ")
    s = s.rstrip()
    lastspace = s.rfind(" ")

    middle = s[firstspace:lastspace+1]
    middle = Trim(middle)

    if len(middle) == 0:
        return ("")

    middle = ProperCase(middle)

    if len(middle) == 1:
        middle = middle + "."
    # RemoveNewLine(s)
    return middle

print("{:<10} {:<10} {:<10}".format("First", "Middle", "Last"))
print("{:<10} {:<10} {:<10}".format("----------", "----------", "----------"))

namesfile = open("07.11 Names.txt","r")
name = namesfile.readline()
while name != "":
    print("{:<10} {:<10} {:<10}".format(FirstName(name), MiddleName(name), LastName(name)))
    name = namesfile.readline()


