import pyshorteners

link = input("enter the link:")
shortener = pyshorteners.Shortener()

x = shortener.tinyurl.short(link)

print(x)
