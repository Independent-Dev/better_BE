- setup.py

  - python setup.py install

- 변경해야 하는 것

  - env.sh
    - WC_KEY와 WC_SECRET 변경하기
  - ssqaapitest > src > configs > hosts_config.py
    - API_HOSTS와 WOO_API_HOSTS의 host address를 local ipaddress로 변경하기
      - ipconfig getifaddr en0

- 궁금한 것
  - 이거 그냥 local로 돌리면 안 되는 것인가...?? 기껏 해놓고 이게 뭔 짓이야...
    - ampp로 해보았는데 mac에서는 안 돌아갔고, Mamp로 해보았는데 unknown WP_HOST라는 문구가 떠서 좀 찾아보다가 그냥 local로 했는데 돌아갔음. 나중에 내 컴퓨터에 맞춰서 최적화하는 것을 해보고 싶음.
