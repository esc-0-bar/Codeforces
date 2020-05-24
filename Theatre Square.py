"""
Author: Mohammad Shiblee Noman Ahad
Email: hello@iamahad.com
Website: www.iamahad.com
Github: www.github.com/i-am-ahad
"""

n, m , a = input().split(sep=" ")

n = int(n)
m = int(m)
a = int(a)

if a == 1 :
    x = n
    y = m

elif (n < a and m < a) or (n == a and m == a) or m * n == a:
    x = 1
    y = 1

elif n > a and m > a :
    if (n % a) != 0 :
        x = int(n / a) + 1
    else: x = int(n / a)
    if (m % a) != 0 :
        y = int(m / a) + 1
    else: y = int(m / a)

elif n >= a and m <= a :
    x = int(n / a) + 1
    y = 1

elif n <= a and m >= a :
    x = 1
    y = int(m / a) + 1


        
print(x * y)