import sys
from load import load_strings

names = load_strings(sys.argv[1])

search_names = ['Cornelius Reese', 'Courtney Walsh', 'Davin Byrd', 'Dayami English', 'Dominik Rhodes', 'Edgar Galvan', 'Eleanor Moses', 'Elena Randolph', 'Elisa Calderon', 'Emilio Sanchez', 'Frida Mcmillan', 'Gabriela Jackson', 'Geovanni Mcpherson', 'Giovanni Maddox', 'Giovanny Wallace', 'Gretchen Mahoney']

def index_of_item(collection, target):
  for i in range(0, len(collection)):
    if target == collection[i]:
      return i
  return None

for n in search_names:
  index = index_of_item(names, n)
  print(index)
