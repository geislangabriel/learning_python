from pygeocoder import Geocoder
endereco = '337, Avenida Pará, Tucumã, PA'
print(Geocoder('AIzaSyAqwoGKs-yTmffGjyhiCIv_7YTFX4PH0uk').geocode(endereco.coordinates))