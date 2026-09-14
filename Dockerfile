FROM python:3.12-slim
RUN pip install --no-cache-dir pytest==8.4.2 ruff==0.11.13
RUN useradd --uid 10001 --create-home runner && mkdir /workspace && chown runner /workspace
USER 10001:10001
WORKDIR /workspace
