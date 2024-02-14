import phonenumbers
import opencage
import folium
from phonenumber import number

from phonenumbers import geocoder

# track location telephone number
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# track service provider
from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

# track geolocation coordinate
from opencage.geocoder import OpenCageGeocode
key = "982d75589ce04e92b922526d46097b9e"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

themap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(themap)
themap.save('thelocation.html')


