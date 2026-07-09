# DevOps Recruitment Task

Simple HTTP server built with FastAPI, containerized with Docker, with CI/CD via GitHub Actions.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health-check` | Returns `{"status": "ok"}` |
| GET | `/hello-world` | Returns text from `SERVER_HELLO` env variable |

## Run with Docker

```bash
docker build -t zadanie-welyo .
docker run -p 8000:8000 -e SERVER_HELLO="your message" zadanie-welyo
```

Or with Docker Compose:

```bash
SERVER_HELLO="Hello from Welyo!" docker compose up
```
