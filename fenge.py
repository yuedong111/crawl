import os
file=open('allitems.txt','r')
lines=file.readlines()
count=0
for line in lines:
    os.system("echo '"+line+"'>>"+str(count)+".txt")
    if 'Name: CVE' in line:
         count=count+1
print count
file.close()

