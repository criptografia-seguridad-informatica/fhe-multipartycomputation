import numpy as np
import requests
from Pyfhel import Pyfhel, PyCtxt


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
NUMBER_OWNERS = 3
PUBLIC_CONTENT_FOLDER = './pub_content'
MY_NUMBER = 3000
ID_MULTI_PARTY_COMPUTATION = '1000'
MY_ID = 'Mateo'

HE_f = Pyfhel() 
HE_f.load_context(PUBLIC_CONTENT_FOLDER + "/context")
HE_f.load_public_key(PUBLIC_CONTENT_FOLDER + "/pub.key")
HE_f.load_relin_key(PUBLIC_CONTENT_FOLDER + "/relin.key")
HE_f.load_rotate_key(PUBLIC_CONTENT_FOLDER + "/rotate.key")



number_as_array = np.array([MY_NUMBER])
encripted_number = HE_f.encryptInt(number_as_array)
serialized_encr_number = encripted_number.to_bytes().decode('cp437')



r = requests.post('http://'+SERVER_HOST+':'+str(SERVER_PORT)+'/'+ID_MULTI_PARTY_COMPUTATION, json={
    data_owner_id: MY_ID
    hashed_data: serialized_encr_number
})
