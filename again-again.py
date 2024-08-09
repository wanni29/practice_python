#  cabinet
cabinet = {"A-3" : "유재석", "B-100" : "조세호"}

print(cabinet.get("A-3"))
print(cabinet.get("B-100"))
print("C-1" in cabinet)
print("A-3" in cabinet)

cabinet["A-3"] = "김종국"
cabinet["C-1"] = "김태호"
print(cabinet)

print(cabinet.get("C-1"))

del cabinet["C-1"]
print(cabinet)

print(cabinet.keys())
print(cabinet.values())

cabinet.clear()
print(cabinet)