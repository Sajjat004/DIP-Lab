n = int(input())
for i in range(n):
  a = list(map(int, input().split()))
  if a[0] * a[0] == a[2] * a[1]:
    print("Equal")
  else:
    print("Not Equal")