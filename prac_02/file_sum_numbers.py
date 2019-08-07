FILE = "txt_files/number.txt"
source_file = open(FILE, 'r')
result = 0
line1 = source_file.readline()
line2 = source_file.readline()
result = int(line1) + int(line2)
#for line_str in source_file:
    #result += int(line_str)
print("Result: {}".format(result))
source_file.close()
