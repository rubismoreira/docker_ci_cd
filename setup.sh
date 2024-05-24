docker-compose up --build -d
docker-compose logs -f authn_tests authz_tests content_tests

docker-compose down