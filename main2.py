from typing import Annotated

import uvicorn
from fastapi import FastAPI, Path, Cookie, Header, Request
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: str | None = None,
        item: Item | None = None,
        ads_id: Annotated[str | None, Cookie()] = None,
        user_agent: Annotated[str | None, Header()] = None,
        request: Request | None = None
):
    """

    :type request: object
    """
    results = {"item_id": item_id}
    print(type(ads_id))
    print("--------" + request.client.host)
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if ads_id:
        results.update({"ads_id": ads_id})
    if user_agent:
        results.update({"user-agent": user_agent})
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
