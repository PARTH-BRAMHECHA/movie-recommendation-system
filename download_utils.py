import gdown
import os

def download_files():
    files = {
        "movies_list.pkl": "1ENIoe5po9YB5Z-JCcQl87fr2l6PeAHMo",   # Replace with actual ID
        "similarity.pkl": "1ex89v7kguzpKD0X3ieQWgERiMCnUqKiQ",   # Replace with actual ID
    }

    for filename, file_id in files.items():
        if not os.path.exists(filename):
            url = f"https://drive.google.com/uc?id={file_id}"
            print(f"Downloading {filename}...")
            gdown.download(url, filename, quiet=False)
