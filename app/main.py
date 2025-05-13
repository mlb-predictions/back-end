from dotenv import load_dotenv
from fastapi import Depends, FastAPI


#app = FastAPI(dependencies=[Depends(get_query_token)])
#load_dotenv()

app = FastAPI()
# print(f"Running in {config.environment} mode")

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}