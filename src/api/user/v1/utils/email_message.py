from datetime import datetime, timedelta
from email.mime.text import MIMEText
import smtplib

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError

from src.config import (
    SECRET_KEY, SMTP_SERVER, SMTP_PASSWORD, SMTP_PORT, SMTP_USER
)


def create_invite_token(email: str) -> str:
    expire = datetime.utcnow() + timedelta(hours=24)
    payload = { 
        'sub': email,
        'exp': expire
    }
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'
    )
    return token


def send_invite_email(email: str, invite_token: str):
    msg = MIMEText(f'Your secret key {invite_token}')
    msg['Subject'] = 'Hello new user!'
    msg['From'] = SMTP_USER
    msg['To'] = email

    print(invite_token)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(SMTP_USER, email, msg.as_string())


def validate_invite_token(email: str, invite_token: str) -> bool:
    try:
        payload = jwt.decode(invite_token, SECRET_KEY, algorithms=['HS256'])
        if payload['sub'] != email:
            return False
        return True
    except (ExpiredSignatureError, InvalidTokenError):
        return False
