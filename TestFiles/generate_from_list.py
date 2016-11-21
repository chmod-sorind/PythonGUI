list_1 = ['Joseph', 'Glen', 'Sally']
hB = 'Happy BroadSigning, '

print('-----For Loop-----')
for i in list_1:
    print(hB + i)
print('-----String Concatenation + printing items by list index-----')
print(hB + list_1[0])
print(hB + list_1[1])
print(hB + list_1[2])
print('-----String Concatenation + String Format-----')
print(hB + "{}".format(list_1[0]))
print(hB + "{}".format(list_1[1]))
print(hB + "{}".format(list_1[2]))
print('-----Liest Lenght-----')
len_list_1 = len(list_1)
print(len_list_1)
