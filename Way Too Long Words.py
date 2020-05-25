"""
Author: Mohammad Shiblee Noman Ahad
Email: hello@iamahad.com
Website: www.iamahad.com
Github: www.github.com/i-am-ahad
"""

words = [] #A list for storing words

n = int(input()) # Total no of words

for x in range(n):
    words.append(input())
    if len(words[x]) > 10:
        temp = words[x][0]
        temp = temp + str(len(words[x]) - 2)
        temp = temp + words[x][-1]
        words[x] = temp

for word in words:
    print(word)