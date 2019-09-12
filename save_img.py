import urllib

import  requests

img_url = "https://kfdown.a.aliimg.com/kf/HTB1hpP8QFXXXXacXpXXq6xXFXXXV/230140137/HTB1hpP8QFXXXXacXpXXq6xXFXXXV.jpg"
img_dir = "a.jpg"
'/kf/HTB1YCfWQVXXXXaXXVXXq6xXFXXXk/201487342/HTB1YCfWQVXXXXaXXVXXq6xXFXXXk.jpg?size=87870&amp;height=886&amp;width=960&amp;hash=98da62fc0720ec0478caa27127c6de22'

# urllib.request.urlretrieve(img_url, img_dir)


r = requests.get(img_url,timeout=30)
with open(img_dir, 'wb') as f:
    f.write(r.content)