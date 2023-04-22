# Little API Project

---

- Make sure set API folder as source in Pycharm project
- Enviromental variables: Deploy/.env
- Logs: /logs
- Allure testing is pretty heavy so I will make it optional later

---

## Fast start

### 1. 
    


---

## Enviromental variables
**Deploy/.env**

| Variable             | Description                                                                                                         | Default            |
|----------------------|---------------------------------------------------------------------------------------------------------------------|--------------------|
| API_PORT             | Port number <br/> *`INT`*                                                                                           | `8000`             |
| APP_MODE             | Development mode equipped with fast reload, deeper logging and docs. <br/> *`String`* : `'development'/'production` | `'development'`    |
| LOG_FILE             | Separate log file in logs folder. Later will be changed of log_path. <br/> *`String`* : `'True'/'False`             | `'False'`          |
| COMPOSE_PROJECT_NAME | Name of compose group in docker listing. <br/>*`String`*                                                            | `ltl_api_template` |
| DOCKER               | Launch method. Set on "Docker" for launch in container. <br/> *`String`* : `'True'/'False`                          | `'True'`           |



---

## Known Issues:


#### 1. Example
#### 2. Second Expample

### Usefull commands:

**All tests**: 
```sh
docker compose -f Deploy/main_compose.yml run --rm ltl_api /bin/sh tests/all_tests_comm.sh
```
