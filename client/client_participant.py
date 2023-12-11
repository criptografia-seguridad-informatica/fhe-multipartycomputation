import numpy as np
import requests
from Pyfhel import Pyfhel, PyCtxt
import json

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000
NUMBER_OWNERS = 3
PUBLIC_CONTENT_FOLDER = './pub_content'
MY_NUMBER = 4321
MY_ID = 'Sofii'

HE_f = Pyfhel() 
HE_f.load_context(PUBLIC_CONTENT_FOLDER + "/context")
HE_f.load_public_key(PUBLIC_CONTENT_FOLDER + "/pub.key")
HE_f.load_relin_key(PUBLIC_CONTENT_FOLDER + "/relin.key")
HE_f.load_rotate_key(PUBLIC_CONTENT_FOLDER + "/rotate.key")


with open(PUBLIC_CONTENT_FOLDER+"/mpc_id.json", 'r') as json_file:
    data = json.load(json_file)
    id_multiparty_computation=data['id_created']


number_as_array = np.array([MY_NUMBER])
encripted_number = HE_f.encryptInt(number_as_array)
serialized_encr_number = encripted_number.to_bytes().decode('cp437')



r = requests.post('http://'+SERVER_HOST+':'+str(SERVER_PORT)+'/mutipartycomputation/'+id_multiparty_computation, json={
    'data_owner_id': MY_ID,
    'encrypted_data': serialized_encr_number
})

print(r.json())