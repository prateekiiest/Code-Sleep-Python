import requests

# TODO: Add more status code functionality.


def check_url(url):
    # This function uses status codes to check various states of any website.

    r=requests.get(url)
    if r.status_code == 200:
        return "Website is online."
    elif r.status_code == 300:
        return "Website has different choices and cannot be resolved into one"
    elif r.status_code == 301:
        return "Website has been redirected permanently."
    elif r.status_code == 302:
        return "Website has been redirected temporarily"
    elif r.status_code == 400:
        return "The request could not be understood by the server due to malformed syntax"
    elif r.status_code == 401:
        return "The request requires user authentication"
    elif r.status_code == 403:
        return "Forbidden. The server understood the request, but is refusing to fulfill it"
    elif r.status_code == 404:
        return "Website not found!"
    elif r.status_code == 503:
        return "The web server is unable to handle your HTTP request at the time"

url = input("Please enter a website, inclusive of 'http://' > ")
print(check_url(url))
