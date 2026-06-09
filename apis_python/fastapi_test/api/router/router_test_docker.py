from fastapi import APIRouter

from datetime import datetime


router_docker = APIRouter(tags=["Test Docker"])


@router_docker.get("/docker-data/{user}")
def docker_data_default(user: str):

    datetime_current = datetime.now()
    datetime_str = datetime_current.strftime("%Y-%m-%d %H:%M:%S")

    data = {"user_name": user,
            "status": "ativo",
            "datetime": datetime_str}

    return data
