import dhooks
from utility import settings

url = settings.DISCORD_WEBHOOK_URL

try :
    hook = dhooks.Webhook(url)
except Exception as e:
    print("웹훅 URL이 유효하지 않습니다. , 입력된 디스코드 URL : ",url)

def send_message(message):
    hook.send(message)