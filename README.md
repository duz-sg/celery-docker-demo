# celery-docker demo

### Useful commands
- Start the services `docker-compose up -d --build`
- Check docker status `docker ps`
- Enter service container `docker exec -it celery-docker_worker_1 /bin/bash`
- Scale up `docker-compose up -d --scale worker=2`
- Stop the services `docker-compose down`
