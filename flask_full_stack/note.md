- Basic
  - form에서는 get과 post만을 지원함.

- Concept
  - CORS(Cross Origin Resource Sharing)
    - SOP의 예외조항. SOP는 Same-Origin Policy의 약자로, RFC 6454에 처음 등장한 '같은 출처에서만 리소스를 공유할 수 있다'는 보안 정책.
      - 여기서 Origin은 Protocol, Host, Port Number를 포함함. 즉, 같은 호스트더라도 포트 번호가 다르면 Cross Origin으로 간주.
    - CORS는 브라우저의 구현 스펙에 포함되는 정책. 클라이언트의 요청에 대하여 서버가 응답을 하면, 브라우저가 이 응답을 분석, Cross Origin이면서 CORS 지원 헤더를 가지고 있지 않으면 해당 응답을 버리는 식으로 작동함.
    - [참조](https://evan-moon.github.io/2020/05/21/about-cors/)
  - MPV(Minimum Viable Product): 최소한의 기능을 구현한 제품

- Tools
  - mongoDB는 로그를 저장하기 위한 것
  - mongoDB 설치
    - 중간에 "Your Command Line Tools (CLT) does not support macOS 11."라는 에러가 나서 해결해주어야 했음. [링크](https://flaviocopes.com/how-to-fix-clt-support-macos-11/) 참조
      - 이 에러가 왜 나는 것인지는... 잘 모르겠음...

- 더 찾아보아야 할 것
  - ajax와 axios
  - JS 난독화 방법
  - themeforest.net: 일종의 스톡 템플릿 사이트
  - ORM의 성능
  - brew 명령어에 관하여
    - brew 
  
