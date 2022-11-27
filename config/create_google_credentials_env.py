import json
from urllib.request import urlopen
from os import getenv

def createGoogleCredentialsEnv() -> None:
    json_url = urlopen(getenv("GOOGLE_CREDENTIAL_FILE_LINK"))
    my_json = json.loads(json_url.read())
    
    json_file = open(getenv("GOOGLE_APPLICATION_CREDENTIALS"), "w")
    json_file.write(json.dumps(my_json))
    json_file.close()