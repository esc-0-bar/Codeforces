"""
Author: Mohammad Shiblee Noman Ahad
Email: hello@iamahad.com
Website: www.iamahad.com
Github: www.github.com/i-am-ahad
"""

n , k = input().split(sep=" ")
n = int(n)
k = int(k)
nextRound = 0
zeroPoint = 0
count = 0
points = input().split(sep=" ")

for x in points:
    points[points.index(x)] = int(x)

if points[k-1] == 0:
    for x in points:
        count += 1
        if x == 0:
            zeroPoint += 1            
            if points.index(x) == k-1 or count == k:
                break
    

for x in points:
    if x>0:
        minPoint = points[k-1]
        nextRound = k
        if minPoint != 0:
            for a in range(k,n):
                if points[a] == minPoint:
                    nextRound += 1
        break

nextRound = nextRound - zeroPoint

if nextRound < 0:
    nextRound = 0

print(nextRound)