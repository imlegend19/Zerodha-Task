release: apt-get install -y cron && python manage.py makemigrations && python manage.py migrate && python manage.py crontab add && python manage.py crontab show
web: gunicorn ZerodhaTask.wsgi:application --log-file -
