from os import environ

API_ID = int(environ.get("API_ID", "23621595"))
API_HASH = environ.get("API_HASH", "de904be2b4cd4efe2ea728ded17ca77d")
BOT_TOKEN = environ.get("BOT_TOKEN", "7107488581:AAFAq0temUKSCH2Ou7RE5n9bfRt4HoVJ9KI")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002523462080"))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
OWNER_ID = environ.get("OWNER_ID","https://t.me/BotMaster55") # Yaha owner link do with https://
JOIN_CHANNEL = environ.get("JOIN_CHANNEL","-1002523462080") # Yaha channel link do with https://t.me
UPDATE_CHANNEL = environ.get("UPDATE_CHANNEL","-1002523462080") # With https://

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://dbmongo702:xtb9PzLmv5dstZYG@cluster0.2dxbh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
