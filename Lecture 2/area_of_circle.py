import random

def in_circle(x,y):
  return (x * x + y * y) < 1.0

n = 0
for i in range(0,1000000):
  x = random.random()
  y = random.random()
  if in_circle(x,y):
    n += 1

print (n/1000000.0 * 4.0)