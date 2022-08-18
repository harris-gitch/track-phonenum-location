#from unittest import result
import phonenumbers
from phone import number
import opencage
import folium
from phonenumbers import geocoder

pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
#print country of the phone
print(location)
from phonenumbers import carrier 
service_pro =phonenumbers.parse(number)
#print service of phone number entred
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode

key="enter here your api key from opencagedata.com site"

geocoder=OpenCageGeocode(key)
query=str(location)
results=geocoder.geocode(query)
print(results)
#print the latitude and longitude of the phone location
lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']
print(lat,lng)

#generate html file contain location map of phone num
myMap= folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation.html")
