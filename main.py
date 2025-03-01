from fastapi import FastAPI

app = FastAPI(
    title="Hello World API",
    description="A simple FastAPI Hello World application",
    version="0.1.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
