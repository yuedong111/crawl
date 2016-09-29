import os
try:
	files=os.listdir(os.getcwd())
	for file1 in files:
		if(file1!='xiugai.py'):
    	 	        file=open(file1,'r+')
       	       		lines=file.readlines()
        		for line in lines:
                		if 'Name: CVE-'in line:
                        		num=line[15:]
                  	       	        print num
                       	       	        numstr=int(num)-1
					numstr=str(numstr)
					if len(numstr)==1:
						numstr="000"+numstr
					if len(numstr)==2:
						numstr="00"+numstr
					if len(numstr)==3:
						numstr="0"+numstr
        	                	line=line[0:15]+str(numstr)
                	       	        print line                
					file.seek(-22,2)
					file.truncate()
					file.write(line+"\n")
			file.close()
except Exception,e:
        print e 

