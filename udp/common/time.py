from datetime import datetime

def getFormattedTime():
    t = datetime.utcnow()
    return t.strftime("%H:%M:%S.%f")[:-3]