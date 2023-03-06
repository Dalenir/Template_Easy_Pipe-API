# Little API Project

---

- Make sure set API folder as source in Pycharm project
- Enviromental variables: Deploy/.env
- Logs: /logs

---

## Enviromental variables
**Deploy/.env**

| Variable             | Description                                                                                                                | Default |
|----------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------------|
| API_PORT             | Port number <br/> *`INT`*                                                           | `8008 `               |
| DEBUG_MODE           | Debyg mode for development. More logs, autoreload from disk. <br/> *`String`* : `'True'/'False`        | `True`                |
| COMPOSE_PROJECT_NAME | Name of compose group in docker listing. <br/>*`Строка`*                                    | `Little_API_Project`  |
| DOCKER               | Launch method. Set on "Docker" for launch in container. Setting DEBUG_MODE on False. <br/> *`String`* : `'True'/'False`   | `'True'`              |


---

## Known Issues:


#### 1. Issue 1
#### 1. Issue 2

### Usefull commands:

**All tests**: `docker compose -f Deploy/main_compose.yml run --rm ltl_api /bin/sh tests/all_tests_comm.sh`
