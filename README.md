# Fake Data Prevention with Conventional Cryptographic Tools

## Project Overview

This project demonstrates how digital signatures can be used to detect data tampering. It is a simple web application built with Python and Flask that allows users to compare an original message with a received message.

The application generates an RSA digital signature for the original message and verifies the signature against the received message. If the message has been modified, the verification fails and the application reports that fake data has been detected.

---

## Features

- RSA key generation
- Digital signature creation
- Digital signature verification
- Fake data detection
- Simple Flask web interface

---

## Technologies

- Python 3
- Flask
- Cryptography
- HTML
- CSS

---

## Project Structure

```
fake-data-prevention/
│
├── app.py
├── crypto_utils.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── keys/
│   ├── private_key.pem
│   └── public_key.pem
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

## How It Works

1. The user enters the original message.
2. The application creates a digital signature using the RSA private key.
3. The user enters the received message.
4. The application verifies the signature using the RSA public key.
5. If both messages are identical, the verification succeeds.
6. If the received message has been modified, the verification fails and fake data is detected.

---

## Installation

Install the required libraries using **pip**:

```bash
pip install -r requirements.txt
```

If pip does not work, you can use **Conda**:

```bash
conda install -c conda-forge flask cryptography
```

Run the application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Example

Original message

```
Transfer 100 euros
```

Received message

```
Transfer 100 euros
```

Result

```
Message is authentic.
```

If the received message is changed:

```
Transfer 1000 euros
```

Result

```
Fake data detected.
```

---

## Author

Tursynbek Beisekul 