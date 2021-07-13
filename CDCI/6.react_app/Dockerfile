# Builder Stage: 빌드파일들을 생성하는 것이 목표
FROM node:alpine as builder

WORKDIR /usr/src/app

COPY package.json .

RUN npm install

COPY ./ ./

RUN npm run build

# Run Stage: Nginx를 가동하고, build 파일을 제공함.
FROM nginx
EXPOSE 80
COPY --from=builder /usr/src/app/build /usr/share/nginx/html

