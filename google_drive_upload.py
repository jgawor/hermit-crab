#!/usr/bin/python3

import mimetypes
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

if len(sys.argv) < 2:
    print("Usage: %s FILE" % os.path.basename(sys.argv[0]))
    sys.exit(1)

mimetypes.init()

file = sys.argv[1]

filename = os.path.basename(file)
file_extension = os.path.splitext(filename)[1]
mime_type = mimetypes.types_map[file_extension]

print("Log-in to Google Drive")

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'google-credentials.json')

credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)

print("Uploading %s (%s)" % (file, mime_type))

folder_id='1v-CewZEx7LUM_q82ht-hWZ-cPcoW1XZb'
file_metadata = {'name': filename, 'parents': [folder_id]}
media = MediaFileUpload(file, mime_type)

file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()

file_id = file.get('id')

print("File uploaded: %s" % file_id)
