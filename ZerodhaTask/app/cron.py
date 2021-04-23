import csv
import urllib
import urllib.request
from datetime import datetime, timedelta
from io import BytesIO, TextIOWrapper
from urllib.error import HTTPError
from zipfile import ZipFile

from django.core.cache import cache

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'


def bhavcopy_parser():
    print("inside")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', UA)]
    urllib.request.install_opener(opener)

    date = datetime.strftime(datetime.now() - timedelta(1), '%d%m%y')
    url = f"https://www.bseindia.com/download/BhavCopy/Equity/EQ{date}_CSV.zip"

    try:
        resp = urllib.request.urlopen(url)
        bhavcopy = ZipFile(BytesIO(resp.read()))

        for info in bhavcopy.infolist():
            with bhavcopy.open(info) as fp:
                content = TextIOWrapper(fp)

                reader = csv.DictReader(content)
                for row in reader:
                    cache.set(row['SC_NAME'].strip().lower(), {
                        'code' : row['SC_CODE'],
                        'name' : row['SC_NAME'],
                        'open' : row['OPEN'],
                        'high' : row['HIGH'],
                        'low'  : row['LOW'],
                        'close': row['CLOSE'],
                    })

                content.close()

        print('ye')
    except HTTPError:
        print('error:', url)
    except Exception as e:
        print(e)
