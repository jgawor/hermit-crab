
## Dependencies

1. Install Google Drive Python API
   ```
   sudo pip3 install google-auth google-auth-httplib2 google-api-python-client
   sudo pip3 install --upgrade httplib2==0.15.0
   ```
1. Setup crontab
   ```
   crontab crontab.sample
   ```

1. Setup webserver.service
   ```
   sudo cp webserver.service /etc/systemd/system/
   ```

   To start the service and enable to run at boot run:
   ```
   sudo systemctl enable webserver
   sudo systemctl start webserver
   ```
   
   To see logs run:
   ```
   sudo systemctl status webserver
   ```
