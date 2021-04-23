release: python manage.py makemigrations && python manage.py migrate && python manage.py crontab add
web: gunicorn ZerodhaTask.wsgi:application --log-file -
