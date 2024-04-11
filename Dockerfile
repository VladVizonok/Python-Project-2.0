FROM python:3.12

WORKDIR /app

COPY . .

RUN python3 -m pip install .

EXPOSE 3000

CMD ["python3", "/app/CLI_2_0/main.py"]


