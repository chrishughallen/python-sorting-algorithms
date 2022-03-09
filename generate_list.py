my_file = open("names/sorted.txt", "r")
content_list = my_file.readlines()
output_list = []
for i in content_list:
  output_list.append(i.rstrip('\n'))
print(output_list)