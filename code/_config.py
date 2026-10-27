from os import makedirs, path

# just some utils that force create the data folder (for storing HTML)
# and also have some useful paths

DATA_DIR = "data"

if not path.exists(DATA_DIR):
    makedirs(DATA_DIR)

def getPath(filename: str) -> str:
    return path.join(DATA_DIR, filename)
