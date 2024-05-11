import os
import qbittorrentapi
from qbittorrentapi import Client, TorrentStates
import time
import json

def killClient(qbt_client):
  # os.system('cmd /c "taskkill /im qbittorrent.exe"')
  qbt_client.app_shutdown()

def startClient():
  os.system('cmd /c "start qtshortcut.lnk"')

def displayClientInfo(qbt_client):
  print(f'qBittorrent: {qbt_client.app.version}')
  print(f'qBittorrent Web API: {qbt_client.app.web_api_version}')
  for k,v in qbt_client.app.build_info.items(): print(f'{k}: {v}')

# instantiate a Client using the appropriate WebUI configuration
qbt_client = qbittorrentapi.Client(
    host='localhost',
    port=8080,
    username='admin',
    password='adminadmin',
)

# the Client will automatically acquire/maintain a logged-in state
# in line with any request. therefore, this is not strictly necessary;
# however, you may want to test the provided login credentials.
try:
  qbt_client.auth_log_in()
except qbittorrentapi.LoginFailed as e:
  print(e)

print("got client")


  print("commencing reboot")
  killClient(qbt_client)
  time.sleep(60)
  startClient()

print("done")

