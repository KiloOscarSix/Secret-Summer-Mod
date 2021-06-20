init python:
    def isUpToDate(fileName, url):
        import requests
        import hashlib

        f = open(fileName, "r")
        file = f.read()
        f.close()
        hash = hashlib.sha256((file).encode('utf-8')).hexdigest()

        urlcode = requests.get(url).text
        urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()

        if hash == urlhash:
            return True
        return False

    def upToDate():
        modConfigPath = os.path.join(config.basedir, "game", "modAdditions", "modConfig.txt")
        try:
            return isUpToDate(modConfigPath, "https://raw.githubusercontent.com/KiloOscarSix/Sun-Breed-Mod/main/game/modAdditions/modConfig.txt")
        except:
            return True
