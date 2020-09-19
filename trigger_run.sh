pip3 install --upgrade pip

pip3 install stix2-validator
pip3 install -r requirements.txt

cd IntelAPITest
current_timestamp=`date +"%Y%m%d"`

export LC_ALL=C.UTF-8

chcp 65001
set PYTHONIOENCODING=utf-8
PYTHONHTTPSVERIFY=0 python3 Runner.py
automation_status=$?

python3 ../Writesummary.py

cd ../

mkdir -p reports
cp -rp ../Logs/* reports/.
cp -rp ../Logs/Html/* reports/.
ls -lhrt reports
