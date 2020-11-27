#Given a string,s , of length t that is indexed from 0 to n-1 ,
#print its even-indexed and odd-indexed characters as
#space-separated strings on a single line

t=int(input())

for i in range(t):
    s=str(input())
    print(s[::2],  s[1::2])