import math
if __name__ == "__main__":
     x = int(input())
     count = 0
     if x > 0:
      for i in range(2, x + 1):
            count += math.log10(i)

     else:
       print(0)
     print(math.floor(count) + 1)