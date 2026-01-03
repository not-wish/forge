import hashlib

def hashContent(fileName: str) -> str:
    
    with open(fileName, "rb") as f:
        contents = f.read()

    return hashlib.sha256(contents).hexdigest()