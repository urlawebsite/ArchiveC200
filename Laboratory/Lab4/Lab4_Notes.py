from traceback import print_tb
from typing import Dict
from emoji import emojize

print(emojize(":thumbs_up:"))

#print(list(range(5, 10)))

#print(list(range(0, 10, 2)))

c = 0
ct = 0
example_lst = [[3, 4], ["cs200", 9.58]]
#example_lst2 = ["tim", "joe", "jim"]
#lst3 = [['a', 'b'], ['v', 'z']]
# for i in range(len(example_lst)):
##print("The fighter at Index Location " + str(i) + " is " + example_lst2[i])
#
# for i in lst3:
# print(i)
# for j in i:
# print(j)
##print("outer loop " + str(i) + " and inner lopp " + str(j))

# for i in example_lst:
##    print("iteration nummber: " + str(c))
# print(i)
##    c += 1
# if len(i) > 1 and type(i) == list:
##        print("iteration sublist: " + str(ct))
# print(i[1])

# for item in example_lst:
# if type(item) == str:
##        print(item)#

#password = ''
#i = 0
#lst = ['p', 'a', 's', 's', 'w', 'o', 'r', 'd', 'a', 'b', 'c']
# while password != 'password':
#    password += lst[i]
#    i += 1
# print(password)
# print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# dict = {
#    'item1': 55,
#    'item2': 24,
#    'item3': 122,
#    'item4': 55
# }
#dict['item6'] = 33
# print(dict)

#dict['item1'] = 45
# print(dict)

# print(dict['item1'])

# print(dict.values())

# for key in dict:
#    print(key)

# for key in dict:
#    value = dict[key]
#    print(value)
