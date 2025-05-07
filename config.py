from os import environ

API_ID = int(environ.get("API_ID", "23621595"))
API_HASH = environ.get("API_HASH", "de904be2b4cd4efe2ea728ded17ca77d")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))
ADMINS = int(environ.get("ADMINS", "7348205141 1249672673"))
OWNER_ID = environ.get("OWNER_ID","https://t.me/BotMaster55")
JOIN_CHANNEL = environ.get("JOIN_CHANNEL","")
UPDATE_CHANNEL = environ.get("UPDATE_CHANNEL","")

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', False))
