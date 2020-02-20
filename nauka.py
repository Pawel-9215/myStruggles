
def half_in_half(sentence):
    char_list = []
    for i in range(0, int(len(sentence)/2), 2):
        char_list.append(sentence[i])
    print("".join(char_list))


list_inp1 = []
how_many = int(input())
#print(type(how_many))
for i in range(1, how_many+1):
    list_inp1.append(input())
for ranges in list_inp1:
    half_in_half(ranges)

            