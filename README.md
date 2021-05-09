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
$ kubectl create -f deployment.yml && kubectl create -f service.yml
```

* To see ip and port
```
$ kubectl get service
```

* to delete
```bash
$ kubectl delete deploy fastapi-lab-deployment && kubectl delete service fastapi-lab-service
```

* Access `http://localhost:8000/docs`