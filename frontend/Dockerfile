
FROM node:lts-alpine3.15 AS builder

WORKDIR /app
COPY package.json .
RUN yarn install
COPY . .
RUN yarn run build

FROM node:lts-alpine3.15
RUN yarn config set network-timeout 5000 -g
RUN yarn global add serve
WORKDIR /app
COPY --from=builder /app/build .
RUN addgroup --system web \
    && adduser --system --ingroup web web
USER web
EXPOSE 3000

