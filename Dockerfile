FROM python:3.12

WORKDIR /CLI_2_0

COPY . .

RUN python3 -m pip install .

ENTRYPOINT ["cli"]



