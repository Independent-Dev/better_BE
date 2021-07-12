* 1강 도커 기본
  * 도커 이미지와 컨테이너
    * 도커 이미지: 코드, 런타임, 시스템 도구, 시스템 라이브러리 및 설정과 같은 응용 프로그램을 실행하는 데 필요한 모든 것(종속성 등)을 포함하는 가볍고 독립적이며 실행가능한 소프트웨어 패키지
      * 1)컨테이너가 시작될 때 실행할 명령어. 
      * 2)컨테이너 하드디스크 로드 후 명령어로 실행할 파일 스냅샷
        * 결국 명령어도 파일 형태로 저장되기에, 1)명령어가 2)스냅샷 안에 포함되어 있어야 함. 
    * 도커 컨테이너: 프로그램을 실행하는 도커 이미지 인스턴스. 이미지는 컨테이너를 생성하고, 이 컨테이너 내부의 프로그램을 명령어로 실행함. 
  * 기본 흐름
    * 도커 클라이언트와 도커 서버(docker demon)
      * 도커 클라이언트에서 명령어를 실행하면 도커 서버에서 프로그램을 실행시켜줌
    * 도커 작동 순서
      * 도커 클라이언트에 명령어 입력 후 도커 서버로 보냄
      * 도커 서버에서 컨테이너를 위한 이미지가 이미 캐시되어 있는지 확인
      * 없으면 도커 허브에서 다운, 있으면 그 이미지로 컨테이너 생성
    * 도커와 기존 가상화 기술 // 머리에 완전히 잘 들어오지는 않는군... 지금 기억나는 것은 도커의 경우 게스트 OS를 이용하지 않고 host OS와 동일한 커널을 사용하기 때문에 더 가볍다는 것. --> <C-group, 네임스페이스를 도커 환경에서 쓸 수 있는 이유>를 보면 host os 위에 리눅스 vm이 있고, 이 리눅스의 커널을 컨테이너가 공유하고 있기 때문에 더 효율적이라는 것으로 보임. 
      * 공통점: 기본 하드웨어에서 격리된 환경 내에 애플리케이션을 배치하는 방법
      * 하이퍼바이저:

* 2강 기본적인 도커 클라이언트 명령어 알아보기
  * docker ps: 실행 중인 컨테이너 나열
    * 실행되지 않은 것도 나열: docker ps - a
    * 특정 포멧으로 나열: docker ps --format "table..."
      * ex: docker ps --format 'table{{.Names}}\t{{.Image}}' 
      
  * 생명주기 관련 명령어
    * 생명주기: 생성 -> 시작 -> 실행 -> 중지 -> 삭제
    * docker create image_name: 이미지의 파일 스냅샷을 컨테이너 하드디스크에 적재
    * docker start container_id/container_name: 시작 명령어 실행 
      * docker start -a adfqreq와 같은 식으로 -a 옵션(attach)을 추가해주어야 실행 결과를 출력함. 
    * docker stop cont_id/cont_name: 하던 작업을 마무리하고(gracefully) stop
    * docker kill: 어떠한 것도 기다리지 않고 stop
    * docker rm container_id/container_name: 컨테이너 삭제 명령어. 중지한 이후에 삭제할 수 있음.
      * docker rm \`docker ps -a -q\`: 모든 컨테이너 삭제
    * docker system prune: 한번에 컨테이너, 이미지, 네트워크 모두 삭제하고 싶을 때 쓰는 명령어. 실행 중인 컨테이너에는 적용되지 않기에 맘 편하게 쓸 수 있음.  
  * docker exec cont_id/cont_name command: 이미 실행 중인 컨테이너에 명령어 전달
    * -it: interactive한 terminal 프로세스를 얻을 수 있게 함. // 사실 이 부분 정확하게는 잘 모르겠음. 
      * docker exec -it 497caccdfb0d sh와 같이 마지막 명령어로 shell을 실행시킬 수도 있음.

* 3강 직접 도커 이미지를 만들어보기
  * 도커 이미지를 생성하는 순서
    * Dockerfile 작성 -> 도커 클라이언트 -> 도커 서버 -> 이미지 생성
  * Dockerfile
    * 도커 이미지를 만들기 위한 설정 파일, 컨테이너가 어떻게 행동해야 하는지에 대한 설정들을 정의함. 
    * Dockerfile을 만드는 순서
      * 파일 스냅샷 만들기: 베이스 이미지 명시 + 추가적으로 필요한 파일 명시
      * 도커 이미지는 여러 개의 레이어로 되어 있는데, 베이스 이미지는 그 중 가장 기반이 되는 일종의 os에 해당하는 레이어라고 할 수 있음. 
  * 빌드 명령어 실행: docker build Dockerfile_path(빌드하고자 하는 파일 path??)
    * 빌드 명령어를 실행하면 base image를 바탕으로 임시 컨테이너가 만들어짐.
      * Dockerfile의 run 부분을 통해 필요한 레이어 추가
    * 컨테이너가 실행되면서 파일 스냅샷 및 최초 실행명령어가 로드됨.
    * 이 컨테이너를 바탕으로 새로운 이미지 생성(첫 베이스 이미지와는 다른 id를 가짐)
    * 생성한 이미지에 기억하기 쉬운 이름을 주려면 빌드 명령어에 -t image_name을 추가해주면 됨. 
    * 도커파일의 이름이 Dockerfile인 경우에는 빌드 시 이름을 넣지 않아도 되지만, 그렇지 않은 경우에는 f 옵션을 사용해주어야 함.
      * ex: docker build -f dockerfile.dev ./ 
    
* 4강 도커를 이용한 간단한 Node.js 어플 만들기
  * COPY 키워드
  * WORKDIR 키워드
  * 네트워크 포트 매핑: p 옵션으로 docker run 명령어를 실행하여야 함.
  * 컨테이너 소스 코드 변경하기
    * COPY를 쓰면 소스코드가 변경될 때마다 이미지를 새로 생성해야 함. 
    * COPY 키워드 대신 run 시에 적절히 -v 옵션을 걸어주면 됨
      * ex)docker run -d -p 4000:8080 -v /usr/src/app/node_modules -v $(pwd):/usr/src/app juju08217/nodejs
      * Q: 이걸 하더라도 copy는 써주어야 하는 것 맞지??
      
* 5강 Docker Compose
  * 컨테이너간의 통신
    * 기본적으로 컨테이너 사이의 통신은 불가. 설정을 추가해주는 것이 필요.
    * 이와 같은 멀티 컨테이너 상황에서 네트워크를 쉽게 생성해주기 위해 Docker Compose를 이용
  * docker-compose up: 도커 컴포즈로 컨테이너 실행
    * 이 명령어는 반드시 docker-compose 파일이 있는 경로에서 실행하여야 함.
    * d 옵션: detached 모드로 앱을 백그라운드에서 실행. so output을 표출하지 않음.
    * --build: 이미지가 있건 없건 이미지를 빌드하고 컨테이너 시
  * etc
    * Redis란? 메모리에 저장하기 때문에 훨씬 빠르고 영속적으로 보관도 가능하다
      * 빠르다는 건 알겠는데 왜 영속적인지는 모르겠음.
    * yml: json과 xml보다 좀 더 읽기 쉬운 포멧
    
* 6강 간단한 어플 실제로 배포해보기
  * 두 개의 도커파일 만들기
  * 쳐야했던 명령어: docker run -it -p 3000:3000 -v /usr/src/app/node_modules -v $(pwd):/usr/src/app juju08217/docker-react-app
    * post, volumes 등의 모든 설정을 docker compose에 저장해놓고 docker-compose up으로 실행할 수도 있음.
  * 개발서버와 다른 운영서버를 써야 하는 이유
    * 개발 서버에는 소스를 변경할 경우 자동으로 전체 앱을 다시 빌드해서 변경 소스를 반영해주는 것과 같이 개발 환경에 특화된 기능들이 있음.
    * 운영에서는 그런 기능들이 없어 더 가볍고, 빠른 Nginx를 사용.
* 참조
  * [도커 강의](https://www.inflearn.com/course/%EB%94%B0%EB%9D%BC%ED%95%98%EB%A9%B0-%EB%B0%B0%EC%9A%B0%EB%8A%94-%EB%8F%84%EC%BB%A4-ci/dashboard)
