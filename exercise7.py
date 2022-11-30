name=input("enter your name")
temp_variable = ""
i=0
while i < len(name):
  if name[i] not in temp_variable:
    temp_variable += name[i]
    print(f"{name[i]} : {name.count(name[i])}")
  i += 1