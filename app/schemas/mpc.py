from pydantic import BaseModel


class MpcSystem(BaseModel):
    number_owners: int
    public_key: str
    relin_key: str
    rotate_key: str
    context: str


class MpcData(BaseModel):
    data_owner_id: str
    hashed_data: str
