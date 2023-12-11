import numpy as np
import requests
from Pyfhel import Pyfhel, PyCtxt
import json

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



with open(PUBLIC_CONTENT_FOLDER+"/mpc_id.json", 'r') as json_file:
    data = json.load(json_file)
    id_multiparty_computation=data['id_created']

r = requests.get('http://'+SERVER_HOST+':'+str(SERVER_PORT)+'/mutipartycomputation/'+id_multiparty_computation)

# print(r.json()['parties'])

resp = r.json()


encypted_result = PyCtxt(pyfhel=HE_f, bytestring=resp['encrypted_result'].encode('cp437'))


res = HE_f.decryptInt(encypted_result)

print("La respuesta es ", res[0])