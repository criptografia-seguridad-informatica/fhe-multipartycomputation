import numpy as np
import requests
from Pyfhel import Pyfhel
import json
from dotenv import load_dotenv
import os

load_dotenv()


SERVER_HOST = os.environ.get("SERVER_HOST")
SERVER_PORT = os.environ.get("SERVER_PORT")
NUMBER_OWNERS = os.environ.get("NUMBER_OWNERS")
PUBLIC_CONTENT_FOLDER = os.environ.get("PUBLIC_CONTENT_FOLDER")
SECRET_KEY_FOLDER = os.environ.get("SECRET_KEY_FOLDER")


HE_client = Pyfhel() 
bfv_params = {
    'scheme': 'BFV',
    'n': 2**13,         # Polynomial modulus degree, the num. of slots per plaintext,
                        #  of elements to be encoded in a single ciphertext in a
                        #  2 by n/2 rectangular matrix (mind this shape for rotations!)
                        #  Typ. 2^D for D in [10, 16]
    't': 65537,         # Plaintext modulus. Encrypted operations happen modulo t
                        #  Must be prime such that t-1 be divisible by 2^N.
    't_bits': 20,       # Number of bits in t. Used to generate a suitable value 
                        #  for t. Overrides t if specified.
    'sec': 128,         # Security parameter. The equivalent length of AES key in bits.
                        #  Sets the ciphertext modulus q, can be one of {128, 192, 256}
                        #  More means more security but also slower computation.
}

HE_client.contextGen(**bfv_params)
HE_client.keyGen()
HE_client.rotateKeyGen()
HE_client.relinKeyGen()

s_public_key = HE_client.to_bytes_public_key()
s_relin_key  = HE_client.to_bytes_relin_key()
s_rotate_key = HE_client.to_bytes_rotate_key()
s_context    = HE_client.to_bytes_context()



HE_client.save_context(PUBLIC_CONTENT_FOLDER + "/context")
HE_client.save_public_key(PUBLIC_CONTENT_FOLDER + "/pub.key")
HE_client.save_secret_key(SECRET_KEY_FOLDER + "/sec.key")
HE_client.save_relin_key(PUBLIC_CONTENT_FOLDER + "/relin.key")
HE_client.save_rotate_key(PUBLIC_CONTENT_FOLDER + "/rotate.key")


r = requests.post('http://'+SERVER_HOST+':'+str(SERVER_PORT)+'/mutipartycomputation/', json={
    'context': s_context.decode('cp437'),
    'public_key': s_public_key.decode('cp437'),
    'relin_key':s_relin_key.decode('cp437'),
    'rotate_key':s_rotate_key.decode('cp437'),
    'number_owners': NUMBER_OWNERS,
})

print(r.json())

with open(PUBLIC_CONTENT_FOLDER + "/mpc_id.json" , 'w') as json_file:
    json.dump(r.json(), json_file)
