import numpy as np
from Pyfhel import Pyfhel, PyCtxt


def create_fhe(s_context, s_public_key, s_relin_key, s_rotate_key):
    HE_server = Pyfhel()
    HE_server.from_bytes_context(s_context.encode('cp437'))
    HE_server.from_bytes_public_key(s_public_key.encode('cp437'))
    HE_server.from_bytes_relin_key(s_relin_key.encode('cp437'))
    HE_server.from_bytes_rotate_key(s_rotate_key.encode('cp437'))
    return HE_server


def encrypted_sum(db_mpc_system, mpc_data):
    HE_server = create_fhe(db_mpc_system.context.decode('utf-8'), 
                           db_mpc_system.public_key.decode('utf-8'),
                           db_mpc_system.relin_key.decode('utf-8'),
                           db_mpc_system.rotate_key.decode('utf-8')
    )
    
    cx1 = PyCtxt(pyfhel=HE_server, bytestring=mpc_data.encode('cp437'))
    cx2 = PyCtxt(pyfhel=HE_server, bytestring=db_mpc_system.result.decode('utf-8').encode('cp437'))

    return (cx1+cx2).to_bytes().decode('cp437')


def zero(s_context, s_public_key, s_relin_key, s_rotate_key):
    HE_server = create_fhe(s_context, s_public_key, s_relin_key, s_rotate_key)
    x = np.array([0])
    cx = HE_server.encryptInt(x)
    return cx.to_bytes().decode('cp437')

