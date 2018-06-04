import requests
import datetime
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import cryptography.exceptions as cryptExceptions
from cryptography.hazmat.backends import default_backend

def verifyTime(message, signature, date):

    signature = int(signature)

    signature = signature.to_bytes(round(signature.bit_length() / 8), byteorder="big")

    with open("public.pem", "rb") as key_file:

        Keys = serialization.load_pem_public_key(
            key_file.read(),
            backend = default_backend()
        )
        pubKey = Keys
        isvalid = True
        signText = str(date) + str(message)
        signText = signText.encode()

        try:
            pubKey.verify(
                signature,
                signText,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )

        except cryptExceptions.InvalidSignature:
            print("invalid signature")
            isvalid = False

        return isvalid

def signTime(messhash):

    messhash = messhash.encode()
    request = requests.post(url, data=messhash)

    return request.text