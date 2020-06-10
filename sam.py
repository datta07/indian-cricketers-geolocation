import requests

address=" Alamuru, Hyderabad, Andhra Pradesh "
print("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=AIzaSyA-6Vypns_l5ACf-vo9C3OrRAAaKUJ6La0")
res = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=AIzaSyA-6Vypns_l5ACf-vo9C3OrRAAaKUJ6La0").json()
print(res)