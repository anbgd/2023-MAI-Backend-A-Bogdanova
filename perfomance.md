<h1>Производительность gunicorn</h1>

Использовалась утилита ab </br>

```shell
ab -n 1000 -c 100 http://127.0.0.1:8000/
```

Benchmarking 127.0.0.1 (be patient)<br/>
Completed 100 requests<br/>
Completed 200 requests<br/>
Completed 300 requests<br/>
Completed 400 requests<br/>
Completed 500 requests<br/>
Completed 600 requests<br/>
Completed 700 requests<br/>
Completed 800 requests<br/>
Completed 900 requests<br/>
Completed 1000 requests<br/>
Finished 1000 requests<br/>


Server Software:        gunicorn<br/>
Server Hostname:        127.0.0.1<br/>
Server Port:            8000<br/>

Document Path:          /<br/>
Document Length:        190000 bytes<br/>

Concurrency Level:      100<br/>
Time taken for tests:   28.930 seconds<br/>
Complete requests:      1000<br/>
Failed requests:        0<br/>
Total transferred:      190143000 bytes<br/>
HTML transferred:       190000000 bytes<br/>
Requests per second:    34.57 [#/sec] (mean)<br/>
Time per request:       2892.956 [ms] (mean)<br/>
Time per request:       28.930 [ms] (mean, across all concurrent requests)<br/>
Transfer rate:          6418.57 [Kbytes/sec] received<br/>

Connection Times (ms)<br/>
|              |min  |mean[+/-sd] |median   |max|
|--------------|-----|------------|---------|---|
|Connect:      |  0 |   1   2.3   |   0   |   12|
|Processing:   | 82 |2743 493.1   |2858   | 3203|
|Waiting:      | 72 |2742 493.1   |2857   | 3202|
|Total:        | 83 |2744 491.9   |2860   | 3203|

Percentage of the requests served within a certain time (ms)<br/>
  50%   2860<br/>
  66%   2893<br/>
  75%   2915<br/>
  80%   2927<br/>
  90%   2959<br/>
  95%   3089<br/>
  98%   3126<br/>
  99%   3140<br/>
 100%   3203 (longest request)<br/>


<h1>Производительность nginx</h1>

Использовалась утилита ab </br>

```shell
ab -n 1000 -c 100 http://127.0.0.1:8080/
```

Benchmarking 127.0.0.1 (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
Completed 1000 requests
Finished 1000 requests


Server Software:        nginx/1.23.4
Server Hostname:        127.0.0.1
Server Port:            8080

Document Path:          /
Document Length:        615 bytes

Concurrency Level:      100
Time taken for tests:   0.385 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      848000 bytes
HTML transferred:       615000 bytes
Requests per second:    2594.19 [#/sec] (mean)
Time per request:       38.548 [ms] (mean)
Time per request:       0.385 [ms] (mean, across all concurrent requests)
Transfer rate:          2148.31 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   3.8      0      15
Processing:     3   35  11.7     34      70
Waiting:        3   34  11.6     34      70
Total:         19   37  10.5     36      72

Percentage of the requests served within a certain time (ms)
  50%     36
  66%     38
  75%     40
  80%     41
  90%     53
  95%     62
  98%     65
  99%     65
 100%     72 (longest request)