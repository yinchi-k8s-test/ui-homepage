FROM ghcr.io/astral-sh/uv:0.4.20-python3.12-bookworm

ENV HOST="ychyperv"
ENV ROOT_PATH="/homepage"

WORKDIR /run
COPY . .
RUN uv sync

EXPOSE 8000

CMD ["uv", "run", "gunicorn", "-b", "0.0.0.0:8000", "-w", "1", "app.ui:server"]
