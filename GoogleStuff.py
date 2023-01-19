import googlemaps

#extracting api key
with open('GMaps.txt', 'r') as F:
    APIkey = F.read()
    F.close()

#helpful tutorial: https://www.youtube.com/watch?v=Q_JAbB1cBJI&t=147s

def getCoordinates(address):
    if address == '' or address == None:
        print('I got a empty string or None value for address')
        return (None, None) #can't get address for either of these inputs
    #grap API key is already loaded and stored in APIkey
    gmaps_client = googlemaps.Client(APIkey)
    geocoderesult = gmaps_client.geocode(address)
    if geocoderesult == []:
        print('Could not get (lat, lng) for address "' + address + '"')
        return (None, None)
    result = geocoderesult[0]
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']
    return (lat, lng)


# for testing
# a = ''
# print(getCoordinates(a))