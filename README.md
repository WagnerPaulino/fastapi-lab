# fastapi-lab

## How to use

* Execute with docker
```bash
./run.sh
```


* Execute with kubernetes(kubctl)
```bash
$ eval $(minikube docker-env)
$ docker build -t fastapi-lab .
$ kubectl apply -f deployment.yml
$ kubectl expose deployment fastapi-lab-deployment --type NodePort
```

* to delete
```bash
$ kubectl delete deploy fastapi-lab-deployment
```

* Access `http://localhost:8000/docs`