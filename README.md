# LittleTracker

## 1. Docker setup
Run `docker-compose up` command

## 2. Setup postgres db and create superuser
Once the container is up and running, use the commands:

    docker container exec -it <container_ID> python manage.py makemigrations

    docker container exec -it <container_ID> python manage.py migrate

    docker container exec -it <container_ID> python manage.py createsuperuser
   
Now you have access to admin page!

## 3. Run tests
To run tests simply use:

  `docker container exec -it <container_ID> python manage.py makemigrations`
