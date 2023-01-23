import os

import uvicorn
from fastapi import FastAPI, Path
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from api_loggers.log import main_logger

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str = Path(default=None, regex="^[a-zA-Z0-9_]*$")):
    return {"message": f"Hello {name}"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc):
    main_logger.infolog.info(f'Error with request {request.url}: RequestValidationError')
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors()[0]['msg']}),
    )


if __name__ == "__main__":
    main_logger.infolog.info('Logger is ready!')

    port = os.getenv('API_PORT', '8008')

    debug_mode = True if os.getenv('DEBUG_MODE') == 'True' else False
    container_enviroment = True if os.getenv('DOCKER') == 'True' else False

    if container_enviroment:
        host = "0.0.0.0"
        port = 8000
    else:
        debug_mode = True
        host = 'localhost'
        port = 8008

    if debug_mode:
        main_logger.infolog.info(f'[S] API ROOT http://localhost:{port}')
        main_logger.infolog.info(f'[S] API DOCS http://localhost:{port}/docs')
        log_level = 'warning'
        reload_policy = False if container_enviroment else True  # Известная проблема см. README (1)
    else:
        main_logger.infolog.info(f'API WIIL BE STARTED IN PRODUCTION MODE AT PORT :{port}')
        log_level = 'info'
        reload_policy = False

    uvicorn.run('main:app', host=host, port=port, log_level=log_level, reload=reload_policy)
