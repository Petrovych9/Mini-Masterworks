import flask
import requests
import folium

from flask import request



def getData(ip):
    if ip == None or len(ip) <= 3:
        flask.flash('Invalid IP', category='error')
        return 0
    else:
        try:
            response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
            data = {
                'IP' : response.get('query'),
                'Country': response.get('country'),
                'City': response.get('city'),
                'Timezone': response.get('timezone'),
                'ZIP': response.get('zip'),
                'Org': response.get('org'),
                'lat': response.get('lat'),
                'lon': response.get('lon'),
            }
            return data
        except requests.exceptions.ConnectionError:
            flask.flash("Check your connection", category='error')

def getLocation(lat,lon):
    area = folium.Map(location=[lat,lon], zoom_start=8)
    folium.Marker([lat,lon]).add_to(area)
    area.save("templates/location.html")
    print("Area created")

def main():
    ip = input("Ented desire IP address:")
    data = getData(ip)
    for k,v in data.items():
        print(f'{k} : {v}')
    getLocation(data['lat'],data['lon'])

if __name__=='__main__':
    main()