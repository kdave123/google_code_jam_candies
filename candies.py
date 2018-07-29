  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for k in range(1, t + 1):
  n, o , d = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  # print("Case #{}: {} {} {}".format(k, n ,  o, d))

  x1, x2, a, b, c, m, l = [int(s) for s in input().split(" ")]
  # print("{} {} {} {} {} {} {}".format(x1, x2, a, b, c, m, l))
  # check out .format's specification for more formatting options
  x = [0] * n
  x[0] = x1
  x[1] = x2
  s = [0] * n
  for i in range(2, n):
      x[i] = ((a * x[i - 1]) + (b * x[i - 2]) + c) % m

  for i in range(0, n):
      s[i] = x[i] + l
      #print(s[i],end=" ")

  maxSweet = [0] * n
  partSweet = [0]*10000
  oddCount = 0
  impos = 1
  u  = 0
  for j in range(0, n):
      oddCount = 0
      for i in range(j, n):

          if (maxSweet[j] + s[i] <= d):
              impos = 0

              if (oddCount == o and s[i]%2!=0):
                  break
              if maxSweet[j]+s[i] <= maxSweet[j]:
                  if j==0:
                      partSweet[u] = s[i]
                  else:
                      partSweet[u] = maxSweet[j]
                  u+=1
              maxSweet[j] += s[i]

              if ((s[i] % 2) != 0):
                  oddCount += 1
                  # print("odd count",s[i]/2, oddCount)
              # else:
              # print("Not ODD")
          else:
              break
  if (impos == 0):
      # print(maxSweet)
      # print(partSweet)
      if sum(y > 0 for y in s) == 0:

          print("Case #{}: {}".format(k, max(s)))
      else:
          print("Case #{}: {}".format(k,max(maxSweet+partSweet)))

  else:
      print("Case #{}: IMPOSIBBLE".format(k))
#KDave
