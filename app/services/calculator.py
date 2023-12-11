import numpy as np
from Pyfhel import Pyfhel


def create_fhe(s_context, s_public_key, s_relin_key, s_rotate_key):
    HE_server = Pyfhel()
    HE_server.from_bytes_context(s_context)
    HE_server.from_bytes_public_key(s_public_key)
    HE_server.from_bytes_relin_key(s_relin_key)
    HE_server.from_bytes_rotate_key(s_rotate_key)
    return HE_server


def encrypted_sum(db_mpc_system, mpc_data):
    HE_server = create_fhe(db_mpc_system.context, db_mpc_system.public_key, db_mpc_system.relin_key, db_mpc_system.rotate_key)
    
    cx1 = PyCtxt(pyfhel=HE_server, bytestring=mpc_data.encode('cp437'))
    cx2 = PyCtxt(pyfhel=HE_server, bytestring=db_mpc_system.result.encode('cp437'))

    return (cx1+cx2).decode('cp437')


def zero(s_context, s_public_key, s_relin_key, s_rotate_key):
    HE_server = create_fhe(s_context, s_public_key, s_relin_key, s_rotate_key)
    x = np.array([0])
    cx = HE_server.encryptInt(x)
    return cx.to_bytes().decode('cp437')

