import random
import math

def write_numbers(value):
  f = open('numbers/' + str(value) +'.txt', "w+")

  for index in range(value):
    n = int(math.ceil(random.random() * value))
    f.write(str(n) + '\n')

write_numbers(10000)
