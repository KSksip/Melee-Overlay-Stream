from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

import json
import uvicorn

app = FastAPI()

app.mount("/overlay", StaticFiles(directory="overlay/", html=True), name="overlay")

@app.get("/getdata")
def get_info():
    with open('data/info.json', 'r') as file:
        json_data = json.load(file)
        return json_data



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)