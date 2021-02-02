<p align="center">

    d888888b d888888b .88b  d88. d88888b .d8888. d88888b d8888b. db    db d888888b  .o88b. d88888b 
    `~~88~~'   `88'   88'YbdP`88 88'     88'  YP 88'     88  `8D 88    88   `88'   d8P  Y8 88'     
       88       88    88  88  88 88ooooo `8bo.   88ooooo 88oobY' Y8    8P    88    8P      88ooooo 
       88       88    88  88  88 88~~~~~   `Y8b. 88~~~~~ 88`8b   `8b  d8'    88    8b      88~~~~~ 
       88      .88.   88  88  88 88.     db   8D 88.     88 `88.  `8bd8'    .88.   Y8b  d8 88.     
       YP    Y888888P YP  YP  YP Y88888P `8888Y' Y88888P 88   YD    YP    Y888888P  `Y88P' Y88888P 

</p>

<p align="center">
    <em>Time Service API is a simple REST API to fetch the current time since epoch.</em>
</p>

<p align="center">

<a href="https://github.com/elkrammer/time-service/actions?query=workflow%3ADocker%20Build" target="_blank">
    <img src="https://github.com/elkrammer/time-service/workflows/Docker%20Build/badge.svg" alt="Build Status">
</a>

---

## Getting Started

### Tech Stack

* Python 3.6+
* FastAPI
* Pydantic
* Poetry
* Uvicorn

### Running the project locally

There's a convenience script at the root of the project `run-locally.sh` which will install all project dependencies and then run the project.

To install the project dependencies manually run `poetry install`.  
To run the project, run `poetry run uvicorn app.main.app --reload`

### Running the project locally using Docker

1. Run `docker build -t time-service:0.1.0` to build the image.
2. Run `docker run -it -p 8000:8000 --rm time-service:0.1.0`

### Validating the service is working

To test the service is working, you can use curl:

```
$ curl -s http://127.0.0.1:8000/ | jq
{
  "message": "Automate all the things!",
  "timestamp": 1612235363
}
```

![curl example](docs/curl.png "curl")

### API Documentation

The project has an interactive API documentation based on [Swagger UI](https://swagger.io/tools/swagger-ui/).
To view the documentation open a browser at `http://127.0.0.1:8000/docs#/` with the application running.

![Swagger](docs/swagger.png "Swagger")

### Kubernetes deployment

TBD
