from sqlalchemy.orm import Session
from ..models.mpc import MpcSystem, MpcData
from ..schemas.mpc import MpcSystem as MpcSystemSchema, MpcData as MpcDataSchema
import uuid
from ..services import calculator


def create_mpc_system(db: Session, mpc_system: MpcSystemSchema):
    random_unique_id = str(uuid.uuid4())
    zero_number = calculator.zero(mpc_system.context, mpc_system.public_key, mpc_system.relin_key, mpc_system.rotate_key)
    
    db_mpc_system = MpcSystem(
        id            = random_unique_id, 
        number_owners = mpc_system.number_owners,
        public_key    = mpc_system.public_key.encode('utf-8'), 
        relin_key     = mpc_system.relin_key.encode('utf-8'), 
        rotate_key    = mpc_system.rotate_key.encode('utf-8'), 
        context       = mpc_system.context.encode('utf-8'),
        result        = zero_number.encode('utf-8')
    )
    db.add(db_mpc_system)
    db.commit()
    db.refresh(db_mpc_system)
    return db_mpc_system


def get_mpc_system(db: Session, mpc_system_id: str):
    return db.query(MpcSystem).filter(MpcSystem.id == mpc_system_id).first()


def update_mpc_system(db: Session, db_mpc_system: MpcSystem, new_result: str, new_data_owner_id: str):
    db_mpc_system.result = new_result.encode('utf-8')
    db_mpc_system.number_data_received = db_mpc_system.number_data_received + 1
    db.commit()
    db.refresh(db_mpc_system)
    
    db_mpc_data = MpcData(
        mpc_system_id = db_mpc_system.id,
        data_owner_id = new_data_owner_id
    )

    db.add(db_mpc_data)
    db.commit()
    db.refresh(db_mpc_data)

    return db_mpc_data


def get_parties(db: Session, mpc_system_id: str):
    mpc_data_list = db.query(MpcData).filter(MpcData.mpc_system_id == mpc_system_id).all()
    return [mpc_data.data_owner_id for mpc_data in mpc_data_list]


