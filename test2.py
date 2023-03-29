import urllib.request

url = "https://animego.org/media/cache/thumbs_250x350/upload/anime/images/62a83ef0a582f827460801.jpg"
filename = "image.jpg"

urllib.request.urlretrieve(url, filename)