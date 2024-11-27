from fastapi import APIRouter, status, HTTPException
from modello.basemodel import Macchinari
from utilità.utils import machinery_collection, plant_collection
from bson.objectid import ObjectId
from utilità.utils import toString

router = APIRouter()

@router.get("/macchinari")
async def get_machinery():
    macchinari = list(machinery_collection.find())
    for macchinario in macchinari:
        macchinario["_id"] = toString(macchinario["_id"])
    return macchinari

@router.get("/macchinari/{id}")
async def get_machinery(id_macchinario: str):
    macchinario = machinery_collection.find_one({"_id": ObjectId(id_macchinario)})
    if macchinario:
        macchinario["_id"] = toString(macchinario["_id"])
        return macchinario
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Macchinario non trovato")

@router.post("/impianti/{id}/macchinari")
async def create_machinery(id_impianto: str, macchinario: Macchinari):
    macchinario.plant_id = id_impianto
    response = machinery_collection.insert_one(macchinario.model_dump())
    plant_collection.update_one({"_id": ObjectId(id_impianto)}, 
                                {"$push": {"machinery": str(response.inserted_id)}})
    return {"_id": toString(response.inserted_id)}