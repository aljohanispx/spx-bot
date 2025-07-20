
import requests

# توكن البوت
TOKEN = '7827995600:AAHkjQIAGETzKYdMMfPYZe-sUaFX8nyj3x0'

# معرف التليجرام الخاص بك
CHAT_ID = '140955030'

# الرسالة اللي تبي ترسلها
message = "📊 تمركز عقود SPX لليوم:\n\n✅ صافي التمركز (Call - Put): -27597\n📉 التوجه العام: هبوطي (Put أكبر من Call)"

# رابط API
url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

# الطلب
response = requests.post(url, data={'chat_id': CHAT_ID, 'text': message})

# تأكيد الإرسال
if response.status_code == 200:
    print("✅ تم إرسال الرسالة بنجاح إلى تليجرام.")
else:
    print("❌ فشل في إرسال الرسالة:", response.text)
