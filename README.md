## Nginx, uWSGI, Django

**Web server** - **WSGI** - **Web Application**

## Requirements

- Python 3.6
- pipenv

### Secret

##### `.secrets/secret_key.json`

```json
{
  "SECRET_KEY":"<Django secret key>"
}
```

- 본 문서는 Docker 개인 학습 저장용으로 업로드되고 있습니다.
- EC2 AWS 에 Docker 를 사용하지 않고 Nginx, uWSGI, Django 의 연결을 만들어 도매인으로 접속해보기

## Installation

```zsh
pipenv install
pipenv shell
cd app
./manage.py runserver
```