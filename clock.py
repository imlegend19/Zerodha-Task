import asyncio
import csv
import urllib.request
from datetime import datetime
from io import BytesIO, TextIOWrapper
from urllib.error import HTTPError
from zipfile import ZipFile
from apscheduler.schedulers.blocking import BlockingScheduler

from ZerodhaTask import REDIS

sched = BlockingScheduler(timezone="Asia/Kolkata")

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'


@sched.scheduled_job('cron', hour=18)
async def timed_job():
    async def add_row_to_redis(row):
        REDIS.hset(row['SC_NAME'].strip(), 'code', row['SC_CODE'])
        REDIS.hset(row['SC_NAME'].strip(), 'open', row['OPEN'])
        REDIS.hset(row['SC_NAME'].strip(), 'high', row['HIGH'])
        REDIS.hset(row['SC_NAME'].strip(), 'low', row['LOW'])
        REDIS.hset(row['SC_NAME'].strip(), 'close', row['CLOSE'])

    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', UA)]
    urllib.request.install_opener(opener)

    date = datetime.strftime(datetime.now(), '%d%m%y')
    url = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{date}_CSV.zip"

    try:
        resp = urllib.request.urlopen(url)
        bhavcopy = ZipFile(BytesIO(resp.read()))

        for info in bhavcopy.infolist():
            with bhavcopy.open(info) as fp:
                content = TextIOWrapper(fp)

                reader = csv.DictReader(content)
                jobs = [add_row_to_redis(r) for r in reader]
                await asyncio.gather(*jobs)

                content.close()
    except HTTPError:
        print('error:', url)
    except Exception as e:
        print(e)


sched.start()
