###########
# BUILDER #
###########

# pull official base image
FROM python:3.10-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update && apk add python3-dev 

# lint
RUN pip install --upgrade pip
# install dependencies
COPY ./requirement.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirement.txt

#########
# FINAL #
#########

# pull official base image
FROM python:3.10-alpine

# create directory for the app user

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
WORKDIR /app
RUN mkdir /app/asset /app/media

# install dependencies
RUN apk update && apk add  bash
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirement.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy project
COPY . .

# chown all the files to the app user
RUN chown -R app:app /app
RUN chmod +x /app/entrypoint.sh
# change to the app user
USER app
EXPOSE 8000
# run entrypoint.prod.sh
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
