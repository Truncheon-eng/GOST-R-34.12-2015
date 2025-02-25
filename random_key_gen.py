import os
import base64

key = os.urandom(32)

key_base64 = base64.b64encode(key).decode('utf-8')

print(key_base64)