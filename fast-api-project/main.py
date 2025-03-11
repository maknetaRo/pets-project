gfrom fastapi import FastAPI

app = FastAPI()

name = 'pies Pixel'

@app.get('/')
async def root():
    return getPetName(name)

def getPetName(name: str):
    return name

