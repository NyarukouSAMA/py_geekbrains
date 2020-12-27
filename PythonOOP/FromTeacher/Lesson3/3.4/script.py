import requests

link = "http://127.0.0.1:5000/secret_page?key="
for n in range(70, 90):
    request_link = link + str(n)
    resp = requests.get(request_link).text
    if resp == "Incorrect key!":
        print("the key " + str(n) + " is incorrect!")
    else:
        print("FOUND: " + str(n))
        break

"http://127.0.0.1:5000/secret_page?key=75"

