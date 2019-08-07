FILE = "txt_files/number.txt"
source_file = open(FILE, 'r')
result = 0
for line_str in source_file:
    result += int(line_str)
print("Result: {}".format(result))
source_file.close()
