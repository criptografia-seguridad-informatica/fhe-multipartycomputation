import numpy as np
import requests
from Pyfhel import Pyfhel, PyCtxt


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
NUMBER_OWNERS = 3
PUBLIC_CONTENT_FOLDER = './pub_content'
SECRET_KEY_FOLDER = './secret_content'


HE_f = Pyfhel() 
HE_f.load_context(PUBLIC_CONTENT_FOLDER + "/context")
HE_f.load_public_key(PUBLIC_CONTENT_FOLDER + "/pub.key")
HE_f.load_relin_key(PUBLIC_CONTENT_FOLDER + "/relin.key")
HE_f.load_rotate_key(PUBLIC_CONTENT_FOLDER + "/rotate.key")
HE_f.load_secret_key(SECRET_KEY_FOLDER + "/sec.key")


