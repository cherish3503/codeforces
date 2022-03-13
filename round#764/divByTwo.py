import sys
def choosePermutation(arr, retArr, depth):
  swtch = False
  if depth == len(arr):
    if sorted(retArr) == list(range(1,n+1)):
      swtch = True
    return swtch
    
  for i in range(len(arr[depth])):
    retArr.append(arr[depth][i])
    swtch = swtch or choosePermutation(arr, retArr, depth+1)
    if swtch:
      return swtch
    retArr.pop()

  return swtch
  
for _ in range(int(input())):
  n = int(sys.stdin.readline())
  inp = list(map(int, sys.stdin.readline().split()))
  arr = [list() for _ in range(n)]
  for i in range(len(arr)):
    k = inp[i]
    while k > 0:
      if k <= n:
        arr[i].append(k)
      k //= 2
  retArr = list()
  if choosePermutation(arr, retArr, 0):
    print('YES')
  else:
    print('NO')
  
