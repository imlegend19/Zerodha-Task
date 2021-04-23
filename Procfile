release: python manage.py makemigrations && python manage.py migrate
web: gunicorn ZerodhaTask.wsgi:application --log-file -
clock: python clock.py
