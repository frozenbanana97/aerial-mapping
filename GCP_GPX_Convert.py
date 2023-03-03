import gpxpy
import pandas as pd
import geopandas as gpd
import os

print('Place 1 GPX file in the desired directory')
print('File location example: \'/home/user/Documents/\', the final slash is important...')
print()
gpxLoc = input('Directory of GPX file: ')

for file in os.listdir(gpxLoc):
    if file.endswith('.gpx'):
        gpxName = file

print()
print('GPX file: ' + gpxName)

gpx = open(gpxLoc + gpxName)
gpx = gpxpy.parse(gpx)
gpx = gpx.to_xml()
df = pd.read_xml(gpx)

df.pop('desc')
df.pop('time')
df.pop('extensions')
if 'hdop' in df.columns:
    df.pop('hdop')
df = df.drop(index=0) # Locus adds an empty row here, remove this line if not needed

shiftPos = df.pop('name')
df.insert(0, 'GCP Label', shiftPos)
df.columns = ['GCP Label', 'Latitude', 'Longitude', 'Elevation (m)']
df.set_index(df.columns[0], drop=True, inplace = True)
df.to_csv(gpxLoc + 'GCP_' + gpxName[:-4] +'.csv')

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
gdf = gdf.set_crs('EPSG:4326')
gdf.to_file(gpxLoc + 'GCP_' + gpxName[:-4] +'.gpkg', driver='GPKG', layer='GCPs')

print()
print(df)
print()
print('Results CSV exported to: ' + gpxLoc + 'GCP_' + gpxName[:-4] +'.csv')
print('Results GPKG exported to: ' + gpxLoc + 'GCP_' + gpxName[:-4] +'.gpkg')