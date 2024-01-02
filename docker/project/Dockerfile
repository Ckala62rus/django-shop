FROM python:3.11

WORKDIR /usr/src/app

COPY src /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y && apt-get install \
    postgresql \
    gcc \
    python3-dev \
    musl-dev -y \
    postgresql \
    postgresql-contrib \
    && apt install mc -y
RUN pip install --upgrade pip


 RUN pip install -r requirements.txt


# COPY ./Docker/project/entrypoint.sh .
# ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
