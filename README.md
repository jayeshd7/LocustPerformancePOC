IntelAPIPerformance test - Locust

Some Basic Tips and Tricks

Run with Web mode -

Example - 
locust -f locust_entity.py


Run with no web mode -

1. locust -f locust_files/my_locust_file.py --no-web -c 1000 -r 100

-c specifies the number of Locust users to spawn, and -r specifies the hatch rate (number of users to spawn per second).

2. CSV Generate in non web

locust -f locust_indicator.py --no-web --csv=mydata -t1m --run-time 5m

locust -f --no-web -c 1000 -r 100 --run-time 1h30m --stop-timeout 99

3.Logging
locust -f locust_indicator.py --logfile=/Users/jayeshdilip.dalal/PycharmProjects/IntelAPIPerformanceTest/IntelAPITest/Logs/keyword.log


4.Distributed Load -

locust -f locust_indicator.py --no-web -c 1000 -r 100 --csv=mydata -t 5m --step-load --step-clients 10  --step-time 60s
