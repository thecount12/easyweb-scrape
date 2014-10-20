#!/usr/bin/python

import urllib2
import urllib
import re
from BeautifulSoup import BeautifulSoup
import codecs 
import time

myread=raw_input("Enter textfile name of URLs: ")
mysite=open(myread,"r")
start=time.time()
#mysite=open("Untitled1.csv","r")
w=open("result.dat","a")
derror=open("error.dat","a")
#**************** first half create array of links exclude png gif etc and stay in same domain
ar=[]
for i in mysite.readlines():
	if 'www' in i:
		domain=i.replace("www.","")
	else:
		domain=i
	ndomain=domain.split(".")
	st=ndomain[0]
	newdomain=st.split("http://")
	print "checking to add to array: %s" % i
	try:	
		website=urllib2.urlopen(i)
		html=website.read()
		links=re.findall('"((http|ftp)s?://.*?)"',html)
		for z in links:
			print "creating array of links for domain"
			print "."
			if newdomain[1] in z[0]: # newdomain is same domain
				alist=['.ico','.jpg','.gif','.png','.css','.xml']
				if all((w not in z[0] for w in alist)): 
					print z[0]
					ar.append(z[0])
	except:
		print "could not connect to %s" % st
		derror.write(st+"\n")	
		pass

derror.close()

#*************** iterate through array write to file on each iteration
for it in ar: 
	w=open("result.dat","a")
	print "working on:%s " % it
	try:
		content=urllib.urlopen(it).readlines()
		for jt in content:
			if '@' in jt:
				soupt=BeautifulSoup(jt.decode('utf-8','ignore'))
				#print soupt
				for linkt in soupt.findAll("a",text=True):
					if ('@' in linkt and '.' in linkt):
						print "_____"
						print linkt
						print "------"
						#re.findall(r"\+\d{2}\s?0?\d{10}",linkt) #phone
						foundemailt=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",linkt)
						if len(foundemailt)!=0:
							fix=it.replace("\n","")
							pkgt=fix+","+foundemailt[0]
							print "data2: %s" % pkgt 
							w.write(pkgt+"\n")
							w.close()
	except:
		pass

mysite.close()

endtime=time.time()
complete=endtime-start
print "time seconds: %d" % complete 
print "time minutes: %f" % float(complete/60)
print "time hours: %f" % float((complete/60)/60)
