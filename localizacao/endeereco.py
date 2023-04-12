from pygeocoder import Geocoder

endereco = 'avenida paulista, 100 Sao Paulo'
resultado = Geocoder(AIzaSyAqwoGKs-yTmffGjyhiCIv_7YTFX4PH0uk).geocode(endereco)
print(resultado)