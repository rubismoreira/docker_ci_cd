FROM datascientest/fastapi:1.0.0

RUN apt-get update
RUN apt install curl -y