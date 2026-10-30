from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

stations = [
    {
        "id": 1,
        "name": "MSRu",
        "orbit": "Moon",
        "crew": 4
    },
    {
        "id": 2,
        "name": "Mon-key",
        "orbit": "Mars",
        "crew": 6
    },
    {
        "id": 3,
        "name": "Gas",
        "orbit": "Jupiter",
        "crew": 15
    }
]

class Station(BaseModel):
    id: int
    name: str
    orbit: str
    crew: int

class StationCreate(BaseModel):
    name: str
    orbit: str
    crew: int

@app.get("/stations", response_model=list[Station])
def get_stations():
    return stations

@app.post("/stations", response_model=Station, status_code=201)
def create_station(station: StationCreate):
    new_station = station.model_dump()
    new_station["id"] = len(stations) + 1
    stations.append(new_station)
    return  new_station