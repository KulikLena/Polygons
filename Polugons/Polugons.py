from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


from decimal import Decimal
import yandex_geocoder 
from yandex_geocoder import Client
import pandas as pd
from yandex_geocoder import (
    InvalidKey,
    NothingFound,
)

polygon = Polygon([tuple(x) for x in df_poly[['Lat', 'Lon']].to_numpy()])
df_points['Within'] = df_points.apply(lambda x: polygon.contains(Point(x['Lat'], x['Lon'])), axis=1)

def load_dataset():
  citiDF = pd.read_excel('coordinates.xls')
  return citiDF
citiDF = load_dataset()
#print(type(citiDF))
#print(len(citiDF))
locations = citiDF.values.tolist()

client = Client("0a46a34b-d8d4-4088-bf01-5dc08a16664a")

for location in locations:
 try:
    coordinates = client.coordinates(str(location))
    print (coordinates)
 except AttributeError:
    print ("None")
 except ValueError:
     print ("None")

    