- Pytest

  - testing framework for python
    - API testing, UI testing, Unit testing
  - test options
    - -m: 특정한 mark만 테스트
      - pytest -m smoke
      - pytest -m "smoke and reg"
      - pytest -m "smoke or reg"
    - -s: 테스트 내부 print문 출력?!?
    - -h: help. 다른 옵션을 알아봄.
  - fixtures: set of environment or settings
  - tips
    - pytest.ini
      - where should I put pytest.ini: You can use a different pytest configuration using pytest -c but tox. ini and setup. cfg must reside in the top-level directory of your package, next to setup.py
    - PytestUnknownMarkWarning:
      - pytest.ini는 pytest를 실행하는 경로와 동일한 곳에 있어야 하나...??
    - html report: 테스트 결과를 html 형식의 report로 뽑아주는 것
      - pytest --html=demo_report.html
      - pytest --html=demo_report.html --self-contained-html
        - css 데이터를 포함하고 있는 html 파일로 만들어줌.
      - [참고](https://pypi.org/project/pytest-html/)

- Section4

  - setup.py

- Tools

  - WordPress:
    - [more info](https://www.thewordcracker.com/basic/wordpress-introduction/)
  - MAMP(Mac, Apache, MySQL, PHP)
    - Apache, MySQL, PHP를 한번에 설치하여 컴퓨터를 스크립트를 실행할 수 있는 로컬 서버로 만들어주는 것이 MAMP이다.
    - 이 서버를 데이터베이스와 연동, WordPress를 설치하여 WordPress를 쓰는 것이 가능.
      - 물론 설치형이 아닌 가입형으로 하면 MAMP 없이도 WordPress 이용 가능.
  - local wp: Local is a free program that allows you to easily set up a WordPress environment on your local computer, regardless of your skill level or experience
    - [more info](https://wpengine.com/support/local/)
  - woocommerce, woocommerce api
  - sublime

- 그 외 내가 모르는 것
  - setuptools 모듈이 무엇인지, 이건 어떻게 사용해야 하는 것인지
    - python setup.py install or develop은 어떤 의미가 있는 것인가.
  - mac 환경변수 세팅 방법: 이제 정말로 확실하게 알아둘 필요가 있음.
    - 환경변수에는 여러 종류가 있는 것으로 알고 있는데, 각각에 대해서 잘 알 필요가 있음. 
    - export KEY=VALUE
  - test가 될 수 있는 파일 조건 확실하게 알아놓기!!
    - https://stackoverflow.com/questions/37353960/pytest-exits-with-no-error-but-with-collected-0-items
  - authentification: OAuth1.0, 2.0, ect
  - 테스트의 종류: smoke test
