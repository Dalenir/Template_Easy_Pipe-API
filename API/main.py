from fastapi import FastAPI
from uvicorn import Server, Config

from endpoints import example_points
from settings import Settings, main_settings, AppMode
from api_loggers.log import main_logger

docs_url = '/docs' if main_settings.APP_MODE == AppMode.DEV else None
redoc_url = '/redoc' if main_settings.APP_MODE == AppMode.DEV else None

app = FastAPI(
    docs_url=docs_url,
    redoc_url=redoc_url
)

app.include_router(example_points.router)


def server_setup(settings: Settings = main_settings):
    main_logger.infolog.info('Logger is ready!')

    if settings.DOCKER:
        host = "0.0.0.0"
        port = 8000
    else:
        host = 'localhost'
        port = settings.API_PORT
    if settings.APP_MODE == AppMode.DEV:
        main_logger.infolog.info(f'[S] API ROOT http://localhost:{settings.API_PORT}')
        main_logger.infolog.info(f'[S] API DOCS http://localhost:{settings.API_PORT}/docs')
        reload_policy = True
        log_level = 'warning'
    else:
        main_logger.infolog.info(f'API STARTED IN PRODUCTION MODE AT PORT :{settings.API_PORT}')
        log_level = 'info'
        reload_policy = False

    return Server(config=Config('main:app', host=host, port=port, log_level=log_level, reload=reload_policy))


if __name__ == "__main__":
    server = server_setup()
    server.run()
