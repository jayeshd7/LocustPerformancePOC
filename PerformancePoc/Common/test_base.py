# encoding: utf-8

"""
Base class for IntelAPI test.

Provides helper functions for obtaining API objects, raw
API responses via Requests and JSON comparisons
between API responses and requests.
"""

import json
import time
import datetime
import random
import re
import base64
import copy
import urllib

import paramiko
import requests

from . import config

USER = ""
PASS = ""
HEADERS = ""
URI = ""


class TestBase():
    """
    API test classes should inherit from this class.
    """

    def get_headers(self, headers=HEADERS):
        return headers

    def _get_api_creds(self):
        return (USER, PASS)

    def api_delete(self, uri, headers=HEADERS):
        auth = self._get_api_creds()
        return requests.delete(uri, auth=auth, headers=headers, verify=False)

    def api_get(self, uri, headers=HEADERS):
        """
        Return a raw api response for uri.

        :param uri: The URI, including host to be retieved
        """
        auth = self._get_api_creds()
        return requests.get(uri, auth=auth, headers=headers, verify=False)

    def api_post(self, uri, body_model, headers=HEADERS):
        auth = self._get_api_creds()
        body = json.dumps(body_model)
        return requests.post(uri, auth=auth, data=body, headers=headers, verify=False)

    def api_put(self, uri, body_model, headers=HEADERS):
        auth = self._get_api_creds()
        body = json.dumps(body_model)
        return requests.put(uri, auth=auth, data=body, headers=headers, verify=False)

    def run_cli_cmd(self, cmd, ip, user=None, passwd=None):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if user is None and passwd is None:
            (username, password) = self._get_api_creds()
        else:
            (username, password) = (user, passwd)
        ssh.connect(ip, username=username, password=password)
        (_, stdout, stderr) = ssh.exec_command(cmd)
        resp = {'exit_status': stdout.channel.recv_exit_status()}
        resp['stdout'] = stdout.readlines()
        resp['stderr'] = stderr.readlines()
        ssh.close()
        return resp

    def add_args_to_uri(self, uri, **kwargs):
        """
        Add query params to a uri.

        :param uri: The uri to which params are added
        :param **kwargs: Keyword args are added to the URI as query params
        """
        if kwargs:
            args = []
            for (param, value) in kwargs.items():
                if value is None:
                    arg = param
                else:
                    arg = '{0}={1}'.format(param, value)
                args.append(arg)
            if '?' in uri:
                arg_string = '&' + '&'.join(args)
            else:
                arg_string = '?' + '&'.join(args)
            uri += arg_string
        return uri

    def cmd_retry_wrapper(self, cmd, user=None, passwd=None,
                          timeout=60, sleep=1):
        """
        This Method waits for a duration untill the command gets successed
        """
        sleep_time = sleep
        while sleep_time <= timeout:
            try:
                result = self.run_cli_cmd(cmd, user, passwd)
                if result['exit_status'] == 0:
                    break
            except paramiko.ssh_exception.NoValidConnectionsError:
                time.sleep(sleep)
                sleep_time += sleep
                print("cmd execution fails, Retrying...")


    def get_date_from_string_date(self, str_date, date_format='%Y-%m-%d'):
        format_date = datetime.datetime.strptime(str_date, '%Y-%m-%d')
        return format_date

    def sort_by_verification(self, date_list, asending=False, desending=False):
        for i in range(len(date_list)):
            if i < len(date_list)-1:
                if asending:
                    if date_list[i] > date_list[i+1]:
                        return False
                if desending:
                    if date_list[i] < date_list[i+1]:
                        return False
        return True

    def get_epoch_from_string_date(self, format_date):
        epoch = int(time.mktime(time.strptime(format_date, '%Y-%m-%dT%H:%M:%S.%fZ')))
        return epoch



    def sort_avaialble_keys_for_count(self, list_keys):
        data = list()
        for key in list_keys:
            if key == 'id':
                break
            else:
                data.append(key)
        return data

    def remove_html_tags(self, text):
        """Remove html tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)
