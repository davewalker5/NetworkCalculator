FROM python:3.13-slim-bullseye AS runtime

ARG VERSION

COPY subnetcalculator-${VERSION}.0 /opt/subnetcalculator

WORKDIR /opt/subnetcalculator
RUN mkdir -p /usr/local/lib/python3.10/logs

RUN apt-get update -y
RUN pip install subnet_calculator-${VERSION}-py3-none-any.whl

ENTRYPOINT [ "python" ]
CMD [ "-m", "api", "production" ]
