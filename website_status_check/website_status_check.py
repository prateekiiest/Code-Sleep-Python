import urllib2
import socket

def check_url( url, timeout=10 ):
    httpcode =1
    if urllib2.urlopen(url,timeout=timeout).getcode() == 200:
        return "website is online"
    elif urllib2.urlopen(url,timeout=timeout).getcode() == 301:
        return "website was redirected permaanently"
    elif urllib2.urlopen(url,timeout=timeout).getcode() == 404:
        return "website was not found"
print "please enter a website to check the status. don`t forget to add the http://"
site = raw_input()
print check_url(site)
