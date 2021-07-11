# fastapi-lab

## How to use

* Execute with docker
```bash
$ chmod +x run.sh
$ ./run.sh
```


* Execute with kubernetes(kubctl)
```bash
$ eval $(minikube docker-env)
$ docker build -t fastapi-lab .
$ kubectl apply -f deployment.yml && kubectl apply -f service.yml
```

* To see ip and port
```
$ kubectl get service
```

* If you're using minikube
```bash
$ minikube tunnel
```

* In other terminal 
```bash
$ minikube service fastapi-lab-service
```

* to delete
```bash
$ kubectl delete deploy fastapi-lab-deployment && kubectl delete service fastapi-lab-service
```

* Access `http://localhost:8000/docs`

* Run postgres
```
docker run -p 5432:5432 --network host -e POSTGRES_USER="admin" -e POSTGRES_PASSWORD="1" -e POSTGRES_DB="test" --name postgres postgres
```