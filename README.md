# Secure File Sharing System
Asecfile 

## Description
A Django-based web application for secure file upload and download. Files are encrypted using AES (PyCryptodome) before storage and decrypted on download, ensuring security at rest and in transit.

## Features
- Upload files via web portal
- AES encryption of files at rest
- Decryption on download
- Secure file handling
- UUID-based file identification

## Tech Stack
- Django
- PyCryptodome
- SQLite (default, can be changed)
- HTML/CSS (Bootstrap optional)

## Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd FUTURE_CS_03

2. **Install dependencies**
   ```bash
    pip install -r requirements.txt
   
3. **Apply migrations**
    ```bash
    python manage.py migrate

4. **Run the server**
    ```bash
    python manage.py runserver

5. **Access the app**

Go to http://127.0.0.1:8000/

**Usage**
- Upload files via the upload form.
- Download files from the list; files are decrypted automatically.

**Security Overview**
See SECURITY.md for details.

License
MIT
