"""
Author: Mohammad Shiblee Noman Ahad
Email: hello@iamahad.com
Website: www.iamahad.com
Github: www.github.com/i-am-ahad
"""

n = int(input())
problems = []
submit = 0
for x in range(n):
    temp = 0
    problems.append(input().split())
    for y in range(3):
        problems[x][y] = int(problems[x][y])
        temp = temp + problems[x][y]
        if temp == 2 and problems[x][y]!=0:
            submit += 1

print(submit)