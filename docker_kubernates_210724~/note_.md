* Docker client
* Docker server
* Docker Compose: 
  * docker-compose 명령어를 사용함.
  * 도커 컨테이너를 보다 간결한 명령어로, 더 쉽게 사용할 수 있도록 도와주는 것. 
  * 복수의 컨테이너를 실행하고 이들을 자동으로 연결해주는 것.
* Concept
  * namespacing: segmenting features. isolating resources per process
  * control Group: limit amount of resources used per process
    * 리눅스에 있는 feature, 도커는 사실 리눅스 커널이 설치된 리눅스 vm 위에서 돌아가는 것. 
  * container: Container is a process or set of processes(not physical thing) that have grouping of resources that are allocated to your process specifically. 

* docker caching

  * 리눅스 명령어들
    * source 
    * 결국 리눅스 관련 책을 보는 수밖에는 없겠구나...

* docker workflow(dev --push and pull request--> test --push code to Travis CI--(if successful, merge PR to master-->AWS)
  * 이 개발 과정에 docker가 직접적으로 들어가있지는 않지만, 여기서 사용되는 tool들에서 docker를 이용하면 훨씬 개발이 쉬워짐.
  * Travis CI: continuous integration provider. pull down code and run a set of test that you write on your code
