from fastapi import FastAPI
import uvicorn

app = FastAPI()


def main():
    uvicorn.run(app)


if __name__ == "__main__":
    main()
