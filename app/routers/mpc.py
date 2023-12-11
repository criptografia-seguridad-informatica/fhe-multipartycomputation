from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database.database import get_db
from ..schemas.mpc import MpcSystem, MpcData
from ..crud import mpc as crud

router = APIRouter(
    prefix="/mutipartycomputation",
    tags=["Multi Party Computation Sum"]
)

@router.post("/")
async def create_mpc(mpc: MpcSystem, db: Session = Depends(get_db)):
    return crud.create_mpc_system(db, mpc)

# @router.post("/{mpc_id}")
# async def add_mpc_data(mpc_id: str, mpc_data: MpcData, db: Session = Depends(get_db)):
#     db_mpc_system = crud.get_mpc_system(mpc_id)
#     if db_mpc_system is None:
#         raise HTTPException(status_code=404, detail=f"Multi Party Computation Sum with id {mpc_id} not found.")
#     if db_mpc_system.number_owners == db_mpc_system.number_data_received:
#         raise HTTPException(status_code=404, detail=f"Multi Party Computation Sum with id {mpc_id} is already full.")
#     new_sum = hashed_sum(db_mpc_system, db_mpc_system, db_mpc_system.public_key)
    
    
#     return crud.add_mpc_data(db, mpc_data)

# @router.get("/{mpc_id}")
# async def get_mpc_system_result(mpc_id: str, db: Session = Depends(get_db)):
#     db_mpc_system = crud.get_mpc_system(db, mpc_id)
#     if db_mpc_system is None:
#         raise HTTPException(status_code=404, detail="Multi Party Computation Sum with id {mpc_id} not found.")
#     if db_mpc_system.number_owners != db_mpc_system.number_data_received:
#         return ""
