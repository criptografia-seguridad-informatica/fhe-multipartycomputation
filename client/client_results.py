import numpy as np
import requests
from Pyfhel import Pyfhel, PyCtxt
import json
from dotenv import load_dotenv
import os

load_dotenv()


SERVER_HOST = os.environ.get("SERVER_HOST")
SERVER_PORT = os.environ.get("SERVER_PORT")
NUMBER_OWNERS = int(os.environ.get("NUMBER_OWNERS"))
PUBLIC_CONTENT_FOLDER = os.environ.get("PUBLIC_CONTENT_FOLDER")
SECRET_KEY_FOLDER = os.environ.get("SECRET_KEY_FOLDER")


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

resp = r.json()


encypted_result = PyCtxt(pyfhel=HE_f, bytestring=resp['encrypted_result'].encode('cp437'))


res = HE_f.decryptInt(encypted_result)

mean = res[0] / NUMBER_OWNERS
participants = resp['owners']

print("El promedio entre los participantes es ", mean)
print("Los participantes fueron: ", participants)
