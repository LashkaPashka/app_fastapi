from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
from datetime import date


app = FastAPI()

class SHoutel(BaseModel):
    name: int
    data_to: date
    data_from: date


@app.get('/', response_model=list[SHoutel])
def hotel(
        location,
        date_to,
        date_from,
        has_spa: Optional[int] = None,
        stars: Optional[int] = Query(None, ge=1, le=5)

):
    hotel = [
        {
         'name': 'Plaza',
         'data_to': '2020-05-25',
         'data_from': '2020-06-04',
        }
    ]

    return hotel
