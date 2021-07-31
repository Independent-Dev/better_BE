* type
  * Pod
    * grouping of containers with a very similar and common purpose(which must be executed together)
    * container를 run하기 위해 deploy할 수 있는 가장 작은 단위
    * able to have one or more container inside of it.
  * Services
    * set up networking in a k8s cluster
    * subtypes
      * ClusterIP
      * NodePort: expose a container to the outside world(only good for dev purpose)
      * LoadBalancer
* command
  * 설정파일 적용: kubectl apply -f client-node-port.yaml 
    * 여기서 config file은 desire state를 담고 있다고 할 수 있음.
    * 이건 declarative approach라고 할 수 있을 것임. imperative approach는 이것과는 다름.
  * kubectl get pods
  * kubectl delete pod client-pod
  * kubectl logs client-pod

* component
  * master


* yaml 만드는 법: https://lejewk.github.io/yaml-syntax/