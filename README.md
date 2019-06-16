## API comunidad energética

### Install:
pip install -r requiremets.txt

### Run:
pyhton manage.py runserver


### Create docker image:

docker build -t comunidad_energetica .

### Run docker image

docker run -p 8080:8000 -i -t comunidad_energetica


### Endpoints

- http://127.0.0.1:8000/comunidad/
- http://127.0.0.1:8000/comunidad/[id]
- http://127.0.0.1:8000/miembro/
- http://127.0.0.1:8000/miembro/[id]
