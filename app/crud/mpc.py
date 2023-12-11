from sqlalchemy.orm import Session
from ..models.mpc import MpcSystem, MpcData
from ..schemas.mpc import MpcSystem as MpcSystemSchema, MpcData as MpcDataSchema
import uuid


def create_mpc_system(db: Session, mpc_system: MpcSystemSchema):
    random_unique_id = str(uuid.uuid4())
    db_mpc_system = MpcSystem(
        id=random_unique_id, 
        number_owners=mpc_system.number_owners,
        public_key=mpc_system.public_key, 
        relin_key = mpc_system.relin_key, 
        rotate_key = mpc_system.rotate_key, 
        context = mpc_system.context,
    )
    db.add(db_mpc_system)
    db.commit()
    db.refresh(db_mpc_system)
    return db_mpc_system


def get_mpc_system(db: Session, mpc_system_id: str):
    return db.query(MpcSystem).filter(MpcSystem.id == mpc_system_id).first()

def update_mpc_system(db: Session, mpc_system_id: str, new_hashed_salary: str):
    db_employee = db.query(Salary).filter(Salary.id == employee_id).first()
    if db_employee:
        db_employee.hashed_salary = new_hashed_salary
        db.commit()
        db.refresh(db_employee)
    return db_employee
