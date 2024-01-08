import geocoder
import requests

g = geocoder.ip('me')
lat=(g.latlng)
print(g.state)

import secrets

print(secrets.token_urlsafe(16))