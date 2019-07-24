import os
import csv

from ftplib import FTP

from data_source import AbstractDataSource

"""

"""


class VirusHostDB(AbstractDataSource):

    def __init__(self):
        super().__init__()

    _FTP_BASE_URI = "ftp.genome.jp"
    _FILE_DIRECTORY = "/pub/db/virushostdb/"
    _README_FILE = "README"
    _DATA_FILE = "virushostdb.tsv"
    _FILES = [_README_FILE, _DATA_FILE]
    _STORAGE_DIR = "data/"
    _FILE_PREFIX = "virus_host_db_"
    _DATA_PATH = os.path.join(_STORAGE_DIR, _FILE_PREFIX + _DATA_FILE)

    def fetch_data(self, force_reload=False):
        if not os.path.exists(self._DATA_PATH) or force_reload:
            with FTP(self._FTP_BASE_URI) as ftp:
                ftp.login(user="anonymous")
                ftp.cwd(self._FILE_DIRECTORY)
                director_content = ftp.nlst()
                for file in self._FILES:
                    if file in director_content:
                        with open(self._DATA_PATH, 'wb') as f:
                            ftp.retrbinary('RETR ' + file, f.write)
                    else:
                        raise RuntimeError("File {} does not exist on the Virus Host DB server.")

    def read_data(self):
        with open(self._DATA_PATH, "r") as tsvin:
            tsvin = csv.reader(tsvin, delimiter='\t')
            for row in tsvin:
                print(row)


if __name__ == "__main__":
    source = VirusHostDB()
    source.fetch_data(force_reload=False)
    source.read_data()
