text = input("Text: ")

words = text.split(" ")
my_dict = {}

for word in words:
    count = 0
    for i in range(0, len(words), 1):
        if word == words[i]:
            count += 1
    if not word in my_dict:
        my_dict[word] = count
print(my_dict)
for key in sorted(my_dict.keys()):
    print("{0:<10} = {1}".format(key, my_dict[key]))
