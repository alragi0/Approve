from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "24140079"))
    API_HASH = getenv("API_HASH", "d4ba07c6bbfd05e8b52dd77880ff254b")
    BOT_TOKEN = getenv("BOT_TOKEN", "6359085597:AAHzb16c7sKbFJCnJSUPIKQZ_CWCojJF3pY")
    FSUB = getenv("FSUB", "SDBotz")
    CHID = int(getenv("CHID", "-1000112234"))
    SUDO = list(map(int, getenv("6460393623").split()))
    MONGO_URI = getenv("MONGO_URI", "")
    
cfg = Config()
