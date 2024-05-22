'''
#pirnt no. of vowels in given input
a=input()
b=['a','e','i','o','u','A','E','I','O','U']
c=0
for i in a:
    if i in b:
        c=c+1 
print(c)   
'''
#write a pyhton program to print max occurred number in strinG
a=input()
s={}
for i in a:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1 
print(s)
print(s.keys())         
resultantchar=''
resultantfreq=0
for key in s.keys():
    if resultantfreq < s[key]:
        resultantfreq = s[key]
        resultantchar = key 
    elif resultantfreq == s[key] and ord(key) < ord(resultantchar):
        resultantchar = key    
print(resultantchar)        
        
              

