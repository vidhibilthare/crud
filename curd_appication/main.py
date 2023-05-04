List1 = [23,"Car","Apple",43,25,23,69,70,69,43]
List2 = ["Dog","Car",23,70,72,43,59,53,51,37]
List3 = ["House","Mobile","Apple",11,16,17,36,59,53,51,37,36,23]


list4 = List1+List2+List3

finel_list = []

for i in list4:
    if i not in  finel_list:
        finel_list.append(i)
print(finel_list)        


