import requests

# TODO: Add more status code functionality.
def check_url(url):
    '''
    This function uses status codes to check various states of any website.
    '''
    r=requests.get(url)
    if r.status_code==200:
        return "Website is online."
    elif r.status_code==301:
        return "Website has been redirected permanently."
    elif r.status_code==404:
        return "Website not found!"        

url=input("Please enter a website, inclusive of 'http://' > ")
print check_url(url)
