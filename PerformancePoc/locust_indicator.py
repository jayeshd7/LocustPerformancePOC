import datetime
import os
import copy
import locust.stats


from locust import HttpLocust, TaskSet, task, between
from Common.config import config_intel_api
from Common.config_endpoints import indicator_endpoints
from Common.logger import Logger

LOG_FILE = "Logs/{0}_{1}.log".format(os.path.relpath(__file__),
                                     datetime.datetime.now().strftime("%Y-%m-%d-%S"))
logger = Logger().get_logger(os.path.relpath(__file__), LOG_FILE)

headers_indicator = copy.deepcopy(config_intel_api)
headers_indicator['headers']['Accept'] = 'application/stix+json; version=2.1'

locust.stats.CURRENT_RESPONSE_TIME_PERCENTILE_WINDOW = 2


class IndicatorBehaviour(TaskSet):

    @task(1)
    def indicator_objectendpoint(self):
        res = self.client.get(indicator_endpoints['object'],
                        auth=(config_intel_api['username'], config_intel_api['password']),
                        headers=headers_indicator['headers'])
        assert res.status_code == 200
        logger.debug('indicator_objectendpoint %s', res.status_code)

    @task(2)
    def indicator_limitendpoint(self):
        res = self.client.get(indicator_endpoints['limit'],
                        auth=(config_intel_api['username'], config_intel_api['password']),
                        headers=headers_indicator['headers'])
        assert res.status_code == 200
        logger.debug('indicator_limitendpoint %s', res.status_code)

    @task(3)
    def indicator_addedafter(self):
        res = self.client.get(indicator_endpoints['added_after'],
                        auth=(config_intel_api['username'], config_intel_api['password']),
                        headers=headers_indicator['headers'])
        assert res.status_code == 200
        logger.debug('indicator_addedafter %s', res.status_code)


    @task(4)
    def indicator_match_status_active(self):
        res = self.client.get(indicator_endpoints['match_status_active'],
                        auth=(config_intel_api['username'], config_intel_api['password']),
                        headers=headers_indicator['headers'])
        assert res.status_code == 200
        logger.debug('indicator_match_status_active %s', res.status_code)

    @task(5)
    def indicator_match_status_revoked(self):
        res = self.client.get(indicator_endpoints['match_status_revoked'],
                        auth=(config_intel_api['username'], config_intel_api['password']),
                        headers=headers_indicator['headers'])
        assert res.status_code == 200
        logger.debug('indicator_match_status_revoked %s', res.status_code)

    @task(6)
    def indicator_match_type(self):
        res = self.client.get(indicator_endpoints['match_type'],
                        auth=(config_intel_api['username'], config_intel_api['password']),
                        headers=headers_indicator['headers'])
        assert res.status_code == 200
        logger.debug('indicator_match_type %s', res.status_code)


class Indicator(HttpLocust):
    task_set = IndicatorBehaviour
    wait_time = between(5, 15)
    host = config_intel_api['uri']
