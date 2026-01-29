import hashlib

class HashUtility:
    def hash(self, input: str):
        salt = "hfishlihli"
        salted_string = input + salt
        md5_hash = hashlib.md5(salted_string.encode()).hexdigest()
        return md5_hash
