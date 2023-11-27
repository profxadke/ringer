#!/usr/bin/env python3

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from playsound import playsound


api = FastAPI()


@api.get("/")
async def get():
    return FileResponse("index.html")


@api.put("/ring")
async def ring():
    playsound("tone.mp3")
    return {"detail": 200}


if __name__ == "__main__":
    __import__("uvicorn").run("main:api", host="0.0.0.0", port=11111)
