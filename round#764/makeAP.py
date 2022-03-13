# WA

import sys

for _ in range(int(input())):
  a,b,c = map(int, sys.stdin.readline().split())
  if (2*b-a)%c == 0 and 2*b-a != 0: # c*k
      print("YES")
  elif (a+c)%(2*b) == 0: # b*k
    print("YES")
  elif (2*b-c)%a == 0 and 2*b-c != 0: # a*k
    print("YES")
  else:
    print("NO")
