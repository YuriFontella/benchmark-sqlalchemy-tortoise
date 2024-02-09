## TORTOISE x SQLALCHEMY

Benchmark com fastapi

```py
pip install -r requirements.txt
```

```py
uvicorn _tortoise:app --workers 4 --port 6000 --log-level 'error'
```

```py
uvicorn _sqlalchemy:app --workers 4 --port 7000 --log-level 'error'
```

## TORTOISE

```
ab -c 500 -n 5000 http://localhost:6000/data
```

```
Concurrency Level:      500
Time taken for tests:   1.028 seconds
Complete requests:      5000
Failed requests:        0
Total transferred:      985000 bytes
HTML transferred:       265000 bytes
Requests per second:    4727.71 [#/sec] (mean)
Time per request:       105.759 [ms] (mean)
Time per request:       0.212 [ms] (mean, across all concurrent requests)
Transfer rate:          909.53 [Kbytes/sec] received
```

```
time http :6000/million
```

```
HTTP/1.1 200 OK
content-length: 7
content-type: application/json
date: Fri, 09 Feb 2024 18:42:22 GMT
server: uvicorn

1000000



real    0m4,297s
user    0m0,228s
sys     0m0,024s
```

## SQLALCHEMY

```
ab -c 500 -n 5000 http://localhost:7000/data
```

```
Concurrency Level:      500
Time taken for tests:   3.620 seconds
Complete requests:      5000
Failed requests:        0
Total transferred:      1000000 bytes
HTML transferred:       280000 bytes
Requests per second:    1552.82 [#/sec] (mean)
Time per request:       321.994 [ms] (mean)
Time per request:       0.644 [ms] (mean, across all concurrent requests)
Transfer rate:          303.29 [Kbytes/sec] received
```

```
time http :7000/million
```

```
HTTP/1.1 200 OK
content-length: 7
content-type: application/json
date: Fri, 09 Feb 2024 18:45:43 GMT
server: uvicorn

1000000



real    0m11,489s
user    0m0,231s
sys     0m0,020s
```