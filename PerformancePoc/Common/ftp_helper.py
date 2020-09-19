'''
Created on 27-Feb-2020

@author: kapil.awate
'''

import ssl
import requests
from bs4 import BeautifulSoup
import wget


class FtpHelper():
    '''
    FTP helper modules.
    '''

    def get_files_from_http_url(self, url, file_extension="csv"):
        ''' Get files of give extension  '''
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            page = response.text
            soup = BeautifulSoup(page, 'html.parser')
            file_list = [node.get('href') for node in soup.find_all('a')\
                         if node.get('href').endswith(file_extension)]
            return file_list

        return[]

class WgetHelper():
    '''
    Wget Helper modules
    '''

    def wget_download_file(self, url, download_file_location, ssl_certificate_validation=False):
        ''' Download file from Url using wget '''
        if not ssl_certificate_validation:
            create_unverified_https_context = ssl._create_unverified_context
            ssl._create_default_https_context = create_unverified_https_context
            wget.download(url, download_file_location)
