import os
import ftplib
import boto3
import time
from botocore.client import Config
from ftplib import FTP
from dotenv import load_dotenv

load_dotenv()

FTP_HOST = os.getenv("FTP_HOST")
FTP_USER = os.getenv("FTP_USER")
FTP_PASS = os.getenv("FTP_PASS")
FTP_DIR = os.getenv("FTP_DIR")

S3_ENDPOINT = os.getenv("S3_ENDPOINT")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")

def keep_alive(ftp):
    try:
        ftp.voidcmd("NOOP")
    except error_temp:
        ftp.connect(FTP_HOST)
        ftp.login(FTP_USER, FTP_PASS)

def sync_ftp_to_s3(ftp, s3, local_dir, remote_dir, base_dir, last_activity):
    print(f"Синхронизация {remote_dir}")
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    
    files = []
    if time.time() - last_activity > 60:  # Проверка каждые 60 секунд
        keep_alive(ftp)
        last_activity = time.time()

    ftp.cwd(remote_dir)
    ftp.retrlines('LIST', files.append)
    
    for file_info in files:
        parts = file_info.split()
        if len(parts) < 9:
            continue
        file_name = " ".join(parts[8:])
        file_type = parts[0][0]
        
        local_path = os.path.join(local_dir, file_name)
        remote_path = f"{remote_dir}/{file_name}"
        s3_key = remote_path.replace(base_dir, '').lstrip('/')
        
        if file_type == 'd':  # Это директория
            sync_ftp_to_s3(ftp, s3, local_path, remote_path, base_dir, last_activity)
        else:  # Это файл
            if time.time() - last_activity > 60:
                keep_alive(ftp)
                last_activity = time.time()

            with open(local_path, 'wb') as f:
                ftp.retrbinary(f'RETR {file_name}', f.write)
            s3.upload_file(local_path, S3_BUCKET, s3_key)
            print(f"Загружено: {s3_key}")
            os.remove(local_path)
    
    ftp.cwd('..')

if __name__ == "__main__":
  ftp = FTP(FTP_HOST)
  ftp.login(FTP_USER, FTP_PASS)
  s3 = boto3.client('s3', endpoint_url=S3_ENDPOINT, aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_KEY, config=Config(signature_version='s3v4'))


  last_activity = time.time()
  sync_ftp_to_s3(ftp, s3, '/tmp/ftp_sync', FTP_DIR, FTP_DIR, last_activity)
