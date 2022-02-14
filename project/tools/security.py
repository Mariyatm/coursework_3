import hashlib
import base64
import hmac
from flask import current_app


def generate_password_digest(password):
    return hashlib.pbkdf2_hmac(
        hash_name="sha256",
        password=password.encode("utf-8"),
        salt=current_app.config["PWD_HASH_SALT"],
        iterations=current_app.config["PWD_HASH_ITERATIONS"],
    )


def get_password_hash(password):
    return base64.b64encode(generate_password_digest(password)).decode('utf-8')


def check_password(password_hash, other_password):
    return hmac.compare_digest(
        password_hash,
        generate_password_digest(other_password)
    )
