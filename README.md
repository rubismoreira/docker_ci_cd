# docker_ci_cd

How to run

``` bash setup.sh ```

1. This will spin up the containers, the tests containers will run just once we have a health check on the api.
2. After the file stops receiving logs from the 3 tests containers its ready for termination
3. Finally a docker-compose down is called


In this solution there are 2 Dockerfiles

The dockerfile on the root expand on the fastapi and install curl on it.

It was necessary to have a curl client running on it in order to check when the api is functional so the test containers can run against it

In this manner I could solve everything on the docker-compose file

The dockerfile on exam_docker is responsible for containerizing the tests. 

Finally the docker compose spins the 3 containers each one having as entry point the appropriate test

The logs are then saved on the api_test.log file that is leveraged as a volume shared among host and the containers


