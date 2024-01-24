n = input("type a range: ")
n = int(n)
for i in range(1, n): # finds the limit on how many numbers you could have
    if 3%i==0 or 5%i==0 or 7%i==0: # checks to see if i is divisable by 3, 5, 7
        i +=i # incerments ever number that is divisable by 3, 5 or 7
print(i)