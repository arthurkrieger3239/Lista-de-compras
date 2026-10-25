from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, InvalidHashError
import hashlib

gerador_hash = PasswordHasher()

def transformar_senha_em_hash(senha):
    return gerador_hash.hash(senha)

def verificar_senha(senha, senha_salva):
    try:
        return gerador_hash.verify(senha_salva, senha)

    except (VerifyMismatchError, InvalidHashError):
        return False

def transformar_token_em_hash(token):
    return hashlib.sha256(token.encode("utf-8")).hexdigest()