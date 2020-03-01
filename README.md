
## Dependencies

1. Install Google Drive Python API
   ```
   sudo pip3 install google-auth google-auth-httplib2 google-api-python-client
   ```
1. Setup crontab
   ```
   crontab crontab.sample
   ```

1. Setup webserver.service
   ```
   sudo cp webservice.service /etc/systemd/system/
   ```

   To start the service and enable to run at boot run:
   ```
   sudo systemctl enable my_service
   sudo systemctl start webserver
   ```
   
   To see logs run:
   ```
   sudo systemctl status webserver
   ```
