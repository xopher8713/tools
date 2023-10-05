import requests
from bs4 import BeautifulSoup
import urllib
import re
import shutil
import os
import zipfile
import time

url = ""
directory = ""

def parser(url, directory):

    html_page = urllib.request.urlopen(url)
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        filename = link.get('href')
        if "zip" in filename:
            dl_url = "%s%s" % (url, filename)
            zip_download(dl_url, filename, directory)

def zip_download(dl_url, filename, directory):

    error_log = "%serror.log" % (directory)
    try:
        print("INFO: Downloading %s" % (filename))
        output_file = "%s/%s" % (directory, filename)
        if os.path.isfile(output_file):
            print("WARNING: File already downloaded, skipping...")
        else:
            with open(output_file, 'wb') as out_file:
                with urllib.request.urlopen(dl_url) as response:
                    shutil.copyfileobj(response, out_file)
        time.sleep(1)
    except:
        print("ERROR: Failed to download %s" % (filename))
        with open(error_log, 'a') as error_log_file:
            error_log_file.write("%s" % (filename))

def zip_extract_and_delete(directory):
    
    for file in os.listdir(directory):
        if file.endswith("zip"):
            try:
                filename= "%s%s" % (directory, file)
                print("INFO: Extracting and deleting %s" % (file))
                with zipfile.ZipFile(filename, 'r') as zip_file:
                    zip_file.extractall(path = directory)
                    os.remove(filename)
            except:
                print("ERROR: Failed to extract %s" % (file))

parser(url, directory)
zip_extract_and_delete(directory)
