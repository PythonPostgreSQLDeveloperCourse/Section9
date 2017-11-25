# Python and PostgreSQL


## Installing pycopg2

- Python 2.7 already installed
- `pip install psycopg2`

```
PS C:\Users\Jonas> python
Python 2.7.13 |Anaconda custom (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> ^D
PS C:\Users\Jonas> pip install psycopg2
Collecting psycopg2
  Downloading psycopg2-2.7.3.2-cp27-cp27m-win_amd64.whl (987kB)
    81% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-?     | 808kB 7.3MB/s eta 0:00:    82% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-O     | 819kB 6.8MB/s eta 0:00:    84% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-%     | 829kB 7.3MB/s eta 0:00:    85% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-?    | 839kB 6.8MB/s eta 0:0    86% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-O    | 849kB 7.3MB/s eta 0:0    87% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-%    | 860kB 7.3MB/s eta 0:0    88% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-?   | 870kB 7.3MB/s eta 0    89% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-O   | 880kB 6.8MB/s eta 0    90% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-%   | 890kB 7.3MB/s eta 0    91% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-?  | 901kB 6.8MB/s eta    92% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-O  | 911kB 6.8MB/s eta    93% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-%  | 921kB 6.8MB/s eta    94% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-? | 931kB 6.8MB/s e    95% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-O | 942kB 6.8MB/s e    96% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-% | 952kB 6.8MB/s e    97% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-?| 962kB 6.8MB/s    98% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-O| 972kB 6.8MB/s    99% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-%| 983kB 6.8MB/s    100% |â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^â-^| 993kB 1.3MB/s
Installing collected packages: psycopg2
Successfully installed psycopg2-2.7.3.2
```



## Verifying it Works

```
PS C:\Users\Jonas> python
Python 2.7.13 |Anaconda custom (64-bit)| (default, May 11 2017, 13:17:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
Anaconda is brought to you by Continuum Analytics.
Please check out: http://continuum.io/thanks and https://anaconda.org
>>> import psycopg2
>>> connection = psycopg2.connect(database='udemy-learning', user='postgres', password='#N1#Gkq7yWkjnE#H', host='localhost')
>>> connection
<connection object at 0x0000000002DB6570; dsn: 'host=localhost password=xxx user=postgres dbname=udemy-learning', closed: 0>
>>> cursor = connection.cursor()
>>> cursor.execute('SELECT * FROM purchases')
>>> for row in cursor:
...     print row
...
(2, 5, 1)
(3, 6, 1)
(5, 3, 5)
(6, 2, 5)
(8, 2, 4)
(9, 3, 4)
(10, 6, 5)
(11, 6, 5)
>>>
```

## What is a Virtual Environment
