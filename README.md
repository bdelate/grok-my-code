# Grok My Code
Personal portfolio website: [www.grokmycode.com](https://www.grokmycode.com)

Contains background info on me along with code snippets and detail for some of my software development projects.

### Dev setup
```
docker-compose build
docker-compose run web python ./grokmycode/manage.py migrate --settings=grokmycode.settings.dev
docker-compose run web python ./grokmycode/manage.py createsuperuser --settings=grokmycode.settings.dev
docker-compose up
```
