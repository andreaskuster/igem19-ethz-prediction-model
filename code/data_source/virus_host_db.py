from ftplib import FTP

"""

"""

_README_URI = "ftp.genome.jp"


def fetch_data():
    with FTP(_README_URI) as ftp:
        ftp.login(user="anonymous")
        ftp.cwd("/pub/db/virushostdb/")
        test = ftp.nlst()
        with open("data/README", 'wb') as f:
            ftp.retrbinary('RETR ' + "README", f.write)


if __name__ == "__main__":
    fetch_data()
    print("done")