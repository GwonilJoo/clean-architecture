import os
import uvicorn

from application.app import create_app
from application.config import get_config


app = create_app()


if __name__ == "__main__":
    config = get_config()
    uvicorn.run(
        app="main:app",
        host=config.HOST, 
        port=config.PORT,
        reload=config.RELOAD,
        workers=config.WORKERS
    )