import pickle
import requests
import json
from pydantic import BaseModel


items = list()
class Item(BaseModel):
    number: int
    originalTitle: str
    releaseDate: str


def serialize(self, filename):
    with open(filename, "wb") as file:
        pickle.dump(self, file)

def get_data():
    resp = requests.get("https://potterapi-fedeperin.vercel.app/en/books")
    return resp.json()


products = get_data()
for product in products:
    item = Item(**product)
    print(item.dict())
    items.append(item)


serialize(items, filename="book.json")