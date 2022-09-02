
FROM node:lts-alpine3.15 AS builder

RUN addgroup --system web \
    && adduser --system --ingroup web web
USER web

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

EXPOSE 3000
CMD ["serve", "-n", "-p", "3000", "-s", "."]
