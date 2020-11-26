#Given an integer,n , print its first 10 multiples.

n=int(input())

for i in range(1,11):
    result=n*i
    print(n,"x",i,"=",result)