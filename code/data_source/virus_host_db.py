import os
from ftplib import FTP

from data_source import AbstractDataSource

"""

"""


class VirusHostDB(AbstractDataSource):

    def __init__(self):
        super().__init__()

    _FTP_BASE_URI = "ftp.genome.jp"
    _FILE_DIRECTORY = "/pub/db/virushostdb/"
    _FILES = ["README", "virushostdb.tsv"]
    _STORAGE_DIR = "data/"
    _FILE_PREFIX = "virus_host_db_"

    def fetch_data(self):
        with FTP(self._FTP_BASE_URI) as ftp:
            ftp.login(user="anonymous")
            ftp.cwd(self._FILE_DIRECTORY)
            director_content = ftp.nlst()
            for file in self._FILES:
                if file in director_content:
                    with open(os.path.join(self._STORAGE_DIR, self._FILE_PREFIX + file), 'wb') as f:
                        ftp.retrbinary('RETR ' + file, f.write)
                else:
                    raise RuntimeError("File {} does not exist on the Virus Host DB server.")


if __name__ == "__main__":
    source = VirusHostDB()
    source.fetch_data()
