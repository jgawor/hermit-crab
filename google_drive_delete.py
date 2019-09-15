#!/usr/bin/python3

import mimetypes
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

if len(sys.argv) < 2:
    print("Usage: %s FILE" % os.path.basename(sys.argv[0]))
    #sys.exit(1)

filter = sys.argv[1]

print("Log-in to Google Drive")

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'google-credentials.json')

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)


files = []
page_token = None
while True:
    response = drive_service.files().list(q="mimeType='video/mp4' and name contains '%s'" % filter,
                                          spaces='drive',
                                          fields='nextPageToken, files(id, name)',
                                          pageToken=page_token).execute()
    for file in response.get('files', []):
        files.append(file)

    page_token = response.get('nextPageToken', None)
    if page_token is None:
        break

# list files
for file in files:
    file_name = file.get('name')
    file_id = file.get('id')
    print('Delete file: %s (%s)' % (file_name, file_id))
    drive_service.files().delete(fileId=file_id).execute()

