import yfinance as yf
import schedule
import time
from utils import preprocess_data
from model_tft import load_model, predict
from telegram_alerts import send_alert

model = load_model('models/tft_gold_model.h5')

def execute_trading():
    try:
        # دریافت داده‌های لحظه‌ای
        live_data = yf.download("GC=F", period='1d', interval='5m')
        
        # پیش‌پردازش
        processed_data = preprocess_data(live_data)
        
        # پیش‌بینی
        prediction, confidence = predict(model, processed_data)
        
        # ارسال هشدار
        if prediction > 0.92:
            send_alert(f"🚨 سیگنال قوی شناسایی شد! اطمینان: {confidence:.2f}%")
            
    except Exception as e:
        send_alert(f"⚠️ خطا در اجرا: {str(e)}")

# زمان‌بندی اجرای هر 5 دقیقه
schedule.every(5).minutes.do(execute_trading)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)