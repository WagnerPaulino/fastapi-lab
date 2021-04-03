docker rm -f fastapi-lab &&
docker build -t fastapi-lab . &&
docker run  --name fastapi-lab -p 8000:8000 --network host fastapi-lab