import datetime
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import cryptography.exceptions as cryptExceptions
import os.path

def getSig(request):

    PROJECT_DIR= os.path.dirname(__file__)

    with open(PROJECT_DIR + "/private.pem", "rb") as key_file:

        Keys = serialization.load_pem_private_key(
            key_file.read(),
            #practical password would be more secure
            password = b"1234567890",
            backend = default_backend()
        )

        currdate = datetime.date.today()
        signText = str(currdate) + str(request)
        messhash = signText.encode()
        signature = Keys.sign(
            messhash,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        return int.from_bytes(signature, byteorder="big")