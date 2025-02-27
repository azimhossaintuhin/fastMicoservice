from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root(**args):
    print("args", args)
    return {"Welcome ": "Welcome To The New  User Plase  Register"}