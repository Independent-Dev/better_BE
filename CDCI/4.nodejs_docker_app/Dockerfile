# NPM이 들어있는 베이스 이미지
FROM node:10

# 어플리케이션을 위한 소스를 따로 보관할 디렉토리
# 파일이 덮어씌워지고 지저분해지는 것을 막기 위해서
WORKDIR /usr/src/app
# 만약 아래와 같이 없는 존재하지 않는 경로를 설정하면 해당 경로가 생성됨.
# WORKDIR /jinoh/src/app

# 매번 종속성을 다운빋지 않아도 되게끔 package.json을 먼저 copy
# 이건 다른 언어로 작업을 할 때에도 쓸 수 있는 팁으로 보인다
COPY package.json ./

RUN npm install

COPY ./ ./

CMD ["node", "server.js"]