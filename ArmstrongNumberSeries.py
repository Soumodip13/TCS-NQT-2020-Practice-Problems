lower = 1
upper =1000
for i in range(lower, upper + 1):
                          sum = 0
                          temp = i
                          while temp > 0:
                                  digit = temp % 10
                                  sum += digit ** 3
                                  temp //= 10

                          if i == sum:
                                print i,


