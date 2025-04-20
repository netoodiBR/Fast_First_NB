from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Batata frita com cheddar e bacon é uma delicia"}
