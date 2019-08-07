user_name = input("Enter Your Name: ")

FILE = "txt_files/name.txt"

open(FILE, 'w')

input_file = open(FILE, 'w')
print("Your Name is: {}".format(user_name), file=input_file)
input_file.close()

output_file = open(FILE, 'r')
for line_str in output_file:
    print(line_str)
#line = output_file.readline()
#print(line)
output_file.close()


