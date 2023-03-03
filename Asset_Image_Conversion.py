import os
from os import mkdir
from osgeo import gdal

print('File location example: \'/home/user/Documents/\', the final slash is important...')
print()
assetsLoc = input('Directory of assets directories: ')
print('Asset directories location: ' + assetsLoc)

isDir = os.path.isdir(assetsLoc + '/JPEGs')

if isDir == False:
	mkdir(assetsLoc+'/JPEGs')

dsmLoc =  assetsLoc +'odm_dem/dsm.tif'
dtmLoc =  assetsLoc +'/odm_dem/dtm.tif'
orthoLoc =  assetsLoc + '/odm_orthophoto/odm_orthophoto.tif'

saveOptions = []
saveOptions.append("QUALITY=75")

# Obtains a JPEG GDAL driver
jpegDriver = gdal.GetDriverByName("JPEG")   

# Create the .JPG file
# gdal.Translate(
# 	assetsLoc+'/JPEGs/'+ assetsLoc[-20:-5] + '_dsm.jpg',
# 	dsmLoc,
# 	options = saveOptions
# )

# gdal.Translate(
# 	assetsLoc+'/JPEGs/'+ assetsLoc[-20:-5] + '_dtm.jpg',
# 	dtmLoc,
# 	options = saveOptions
# )

gdal.Translate(
	assetsLoc+'/JPEGs/'+ assetsLoc[-20:-5] + '_ortho.jpg',
	orthoLoc,
	options = saveOptions
)