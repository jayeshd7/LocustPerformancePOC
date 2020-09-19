import datetime
import glob
import os

dt = datetime.datetime.now().strftime("%Y-%m-%d-%S")

#get all python files 
files = glob.glob('*.py')


os.system('locust -f --html=Logs/Html/IntelAPI_STAGING_Test%s.html %s' % (dt, files))
