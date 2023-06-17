# QACloudCamp_test_task
## Task description:

### Автоматизация тестирования API. Часть 1
Необходимо подготовить проект с автотестами, которые будут проверять работу всех API-эндпоинтов, описанных ниже.

Технические требования:
API url https://jsonplaceholder.typicode.com/

- Методы, требующие проверки: GET /posts, POST /posts, DELETE /posts
<br>
- Методы могут принимать параметры userId, id, title, body
<br>
- В качестве языка программирования используйте python
<br>
- Добавьте в README инструкцию по поднятию проекта
<br>
- Используйте библиотеку requests, а также pytest

<br>
<br>

### Автоматизация тестирования API. Часть 2

Напишите Dockerfile к своему приложению по проверке API-методов из части 1.

#### Технические требования:
- добавьте команду запуска в README.

## How to work with this repository:

- Clone repository to your machine.

- Navigate to the root folder of the project.
- Create a virtual environment.
- Run command **pip install -r requirements.txt**
- After, execute **pytest --alluredir=allure_result .\tests** to run tests.
- To view the allure report, type the command: **allure serve .\allure_result**



#### Run tests with docker you can use commands:
- docker build -t app .
- docker run app

#### To get an allure report from docker, type the following commands:
- $CONTAINER_ID = (docker ps -a -q | Select-Object -First 1)
- docker cp ${CONTAINER_ID}:/app/allure_result .
- To view the allure report, type the command: **allure serve .\allure_result**
