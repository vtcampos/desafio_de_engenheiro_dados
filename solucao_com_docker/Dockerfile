# Build stage
FROM python:3.7-buster as build-stage

ENV PYTHONUNBUFFERED 1

COPY ./ ./

WORKDIR scripts/

RUN apt-get update && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt 

# Production stage
FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1

COPY --from=build-stage /root/.cache /root/.cache
COPY --from=build-stage /usr/local/lib/python3.7/site-packages /usr/local/lib/python3.7/site-packages
COPY --from=build-stage /scripts /scripts

RUN apt-get update -y && \
    apt-get install -y r-base

RUN R -e "install.packages('read.dbc',dependencies=TRUE, repos='http://cran.rstudio.com/')"

WORKDIR /scripts




