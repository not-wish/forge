import hashlib

def hashContent(fileName: str) -> str:
    
    try:
        with open(fileName, "rb") as f:
            contents = f.read()

        return hashlib.sha256(contents).hexdigest()
    except FileNotFoundError:
        print(f"------------------------------\nThe file: {fileName} could not be hashed since it doesn't exist.\nSkipping the file.\n------------------------------\n")
    
    return ""