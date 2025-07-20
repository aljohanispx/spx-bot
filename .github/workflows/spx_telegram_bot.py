import os
import requests

# قراءة TOKEN و CHAT_ID من Secrets
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

if not TOKEN or not CHAT_ID:
    raise ValueError("❌ لم يتم العثور على TOKEN أو CHAT_ID في المتغيرات البيئية.")

message = """📊 تمركز عقود SPX لليوم:

✅ صافي التمركز (Call - Put): -27597
📉 التوجه العام: هبوطي (Put أكبر من Call)
"""

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
response = requests.post(url, data={'chat_id': CHAT_ID, 'text': message})

if response.status_code == 200:
    print("✅ تم إرسال الرسالة بنجاح إلى تليجرام.")
else:
    print("❌ فشل في إرسال الرسالة:", response.text)
