from fastapi import FastAPI
import uvicorn

from fastapi_test.api.router.router_test_docker import router_docker
from fastapi_test.api.router.router_swagger import router_swagger

api = FastAPI()
api.include_router(router_docker)
api.include_router(router_swagger)

if __name__ == "__main__":

    uvicorn.run(api, host="0.0.0.0", port=8000)
