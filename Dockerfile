FROM ubuntu
RUN apt-get update &&  apt-get install -y python3 python3-pip python3-venv
COPY ./ ./
RUN python3 -m venv .env && ./.env/bin/pip install -r req.txt
EXPOSE 8000
CMD ["./.env/bin/python", "manage.py", "runserver", "8000:8000"]

    