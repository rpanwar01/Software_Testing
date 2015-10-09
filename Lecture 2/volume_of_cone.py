import random

def in_cone(x,y,z):
  return (x * x + y * y) < (1.0 - z)

n = 0
for i in range(0,1000000):
  x = random.random()
  y = random.random()
  z = random.random()
  if in_cone(x,y,z):
    n += 1

n = n/1000000.0 * 4.0

print (n * 2)
print (n * 4)