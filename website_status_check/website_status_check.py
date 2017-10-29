import urllib2 #importing library urllib2 (which user might need to install before running the script)
import socket #importing socket

def check_url( url, timeout=10 ):  #creating function to keep code orginized 
    if urllib2.urlopen(url,timeout=timeout).getcode() == 200:  #this is checking if the return request of urllib2 is 200 which means website is online
        return "website is online" #returns a string 
    elif urllib2.urlopen(url,timeout=timeout).getcode() == 301: #this is checking if the return request of urllib2 is 301 which means website has been permanently redirected
        return "website was redirected permanently" #returns a string
    elif urllib2.urlopen(url,timeout=timeout).getcode() == 404: #this is checking if the return request of urllib2 is 404 which means page was not found
        return "website was not found" #returns a string
print "please enter a website to check the status. don`t forget to add the http://"  #printing prompt line
site = raw_input()  #input string was put into site as a variable 
print check_url(site) #run function with given variable
