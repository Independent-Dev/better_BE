#### 1.Redis introduction
* Redis 기본 명령어(mac)
  * 설치: brew install redis
  * 그 외: brew services [star, stop, restart, list] redis
  * get, set, flush
  * benchmarking performance
    * redis-benchmark
  * 궁금한 것
    * port 변경이 왜 필요한 것일까...
* 참조
  * [Redis mac 설치](https://swiftymind.tistory.com/62)
  * [another link about basic command](https://www.xelloss.pe.kr/265)
  * [Redis prt 추가](https://choseongho93.tistory.com/268)
  * [tutorial](https://www.itpanther.com/redis-beginners-to-advance-deep-dive/)
  * [online Redis cli](https://try.redis.io/)
  
#### 2.Redis Data Types - Deep Dive
  * Redis is key sensitive
  * 기본 연산
    * get, set key value [EX seconds], keys *, del key, incr key
      * TTL은 session에 쓸 수 있을 것 같다.
    * mget, mset,  // this is faster
    * exists key
    * expire key seconds, persist key
      * set key value EX seconds와 같은 형식으로 만료초를 설정할 수도 있음.
    * flushall: delete all the keys in Redis
  * 리스트 연산
    * lpush key values, rpush key values, lrange key start end
      * start와 end index 둘 다 포함. 
    * lpop key, rpop key, ltrim key start end
  * hash
    * hset hash_name key1 value1 key2 value2 ..., hget hash_name key
    * hmget hash_name keys
    * 이걸 대체 왜 쓰는 것인가
  * set: 중복, 순서 없음. 
    * sadd set_name member1, member2
    * scard set_name, smembers set_name
    * sdiff set_name1 set_name2: set_name1 - set_name2
    * sismember set_name member
    * smove set_name1 set_name2 member: 특정 멤버를 mv 시키는 것. 
    * spop set_name [count]: count만큼 임의 멤버를 제거
    * srem set_name member
  * checking command history: cat ~/.rediscli_history
  * transaction 관련 명령어
    * watch, multi, exec, discard
    
