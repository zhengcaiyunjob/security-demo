import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from itsdangerous import TimedSerializer

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


s = TimedSerializer('secret_key')

data = {"username": "bob", "email": "bob@123.com"}
token = s.dumps(data, salt="123")
print(token)
try:
    data = s.loads(token, salt="123", max_age=3600)
    print(data)
except Exception:
    print("err")


@app.get("/")
async def index():
    """
    注册一个根路径
    :return:
    """
    return {"message": "Hello World"}


@app.get("/info")
async def info():
    """
    项目信息
    :return:
    """
    a = "a"
    b = a + "b"
    print(b)
    return {
        "app_name": "FastAPI框架学习",
        "app_version": "v0.0.1"
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "item_name": Item.name, "q": q}


@app.post("/items")
async def create_time(item: Item):
    print('dddd' + item)
    print(item)
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
