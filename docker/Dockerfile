FROM python:3.10-slim-bullseye AS runtime

COPY subnetcalculator-1.3.0.0 /opt/subnetcalculator-1.3.0.0

WORKDIR /opt/subnetcalculator-1.3.0.0
RUN mkdir -p /usr/local/lib/python3.10/logs

RUN apt-get update -y
RUN pip install -r requirements.txt
RUN pip install subnet_calculator-1.3.0-py3-none-any.whl

ENTRYPOINT [ "python" ]
CMD [ "-m", "api", "production" ]
