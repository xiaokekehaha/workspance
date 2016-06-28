export PYTHONTEMP="/var/pythoncode/bsteelmanagement/"
pid=`ps -ef|grep "python"|grep "$PYTHONTEMP"|grep -v "grep"|awk '{print $2}'`
if [ "$pid" = "" ] ; then
  echo "no tomcat pid alive"
else
  echo "kill pid $pid now"
  kill -9 $pid
fi
python /var/pythoncode/bsteelmanagement/manage.py runfcgi host=192.168.110.150 port=8011 --settings=bsteelmanagement.settings