import os
import requests

# قراءة التوكن ومعرف الشات من متغيرات البيئة (GitHub Secrets)
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# تحقق من وجود القيم
if not TOKEN or not CHAT_ID:
    raise ValueError("❌ لم يتم العثور على TOKEN أو CHAT_ID في البيئة!")

# نص الرسالة
message = """📊 تمركز عقود SPX لليوم:

✅ صافي التمركز (Call - Put): -27597
📉 التوجه العام: هبوطي (Put أكبر من Call)
"""

# إعداد رابط الطلب
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

# إرسال الطلب إلى تليجرام
response = requests.post(url, data={'chat_id': CHAT_ID, 'text': message})

# التحقق من نجاح الإرسال
if response.status_code == 200:
    print("✅ تم إرسال الرسالة بنجاح إلى تليجرام.")
else:
    print("❌ فشل في إرسال الرسالة:", response.text)
