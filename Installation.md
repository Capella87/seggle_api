# 설치 가이드

## 설치하기

## 설치 후 마이그레이션
1. 먼저 admin, auth, contenttypes, sessions, 를 마이그레이션을 한다.
```commandline
python manage.py migrate [대상]
```
admin을 마이그레이션을 할 때 오류가 발생할 수 있는데 이는 다음과 같은 명령어를 치면 된다.

```commandline
python manage.py migrate admin --fake
python manage.py migrate admin
```

2. account, announcements 앱을 마이그레이션한다.

```commandline
python manage.py makemigrations account
python manage.py migrate account
```
마이그레이션할 때 SeggleUser 테이블이 없다는 투의 오류가 발생하면,
settings.py 내의 'INSTALLED_APPS'에서 'django.contrib.admin'을 주석 처리하고, urls.py에서 이것과 관련된 모든 URL 설정을
모두 임시로 주석 처리한 후 마이그레이션을 한다. 완료되면 주석 처리를 전부 해제하면 된다.

3. Admin 계정 생성

다음과 같은 명령어를 쳐서 관리자 계정을 만들면 설치 작업은 끝난다.
```commandline
pyuthon manage.py createsuperuser
```

## 출처
* <https://stackoverflow.com/questions/33086444/django-1-8-migrate-is-not-creating-tables>
* <https://stackoverflow.com/questions/44651760/django-db-migrations-exceptions-inconsistentmigrationhistory?answertab=trending#tab-top>