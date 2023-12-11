from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..schemas.mpc import MpcSystem, MpcData
from ..crud import mpc as crud
from ..services import calculator


router = APIRouter(
    prefix="/mutipartycomputation",
    tags=["Multi Party Computation Sum"]
)


@router.post("/")
async def create_mpc(mpc: MpcSystem, db: Session = Depends(get_db)):
    created = crud.create_mpc_system(db, mpc)
    return {
        'id_created': created.id
    }


@router.post("/{mpc_id}")
async def add_mpc_data(mpc_id: str, mpc_data: MpcData, db: Session = Depends(get_db)):
    db_mpc_system = crud.get_mpc_system(db, mpc_id)
    if db_mpc_system is None:
        raise HTTPException(status_code=404, detail=f"Multi Party Computation Sum with id {mpc_id} not found.")
    if db_mpc_system.number_owners == db_mpc_system.number_data_received:
        raise HTTPException(status_code=404, detail=f"Multi Party Computation Sum with id {mpc_id} is already full.")
    parties = crud.get_parties(db, mpc_id)
    print(parties)
    if mpc_data.data_owner_id in parties:
        raise HTTPException(status_code=404, detail=f"Owner {mpc_data.data_owner_id} has already sent data to"
                                                    f" Multi Party Computation Sum with id {mpc_id}.")
    new_sum = calculator.encrypted_sum(db_mpc_system, mpc_data.hashed_data)
    updated = crud.update_mpc_system(db, db_mpc_system, new_sum, mpc_data.data_owner_id)


@router.get("/{mpc_id}")
async def get_mpc_system_result(mpc_id: str, db: Session = Depends(get_db)):
    db_mpc_system = crud.get_mpc_system(db, mpc_id)
    print("Se obtiene el system")
    if db_mpc_system is None:
        raise HTTPException(status_code=404, detail="Multi Party Computation Sum with id {mpc_id} not found.")
    if db_mpc_system.number_owners != db_mpc_system.number_data_received:
        raise HTTPException(status_code=404, detail=f"Multi Party Computation Sum with id {mpc_id} is not yet full.")
    print("Por buscar parties")

    parties = crud.get_parties(db, mpc_id)
    print("Se obtienen parties")
    return {
        # 'parties': parties,
        'result': db_mpc_system.result,
    }
