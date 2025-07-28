from time import sleep
from datetime import datetime
import MetaTrader5 as mt5

# Login details
login = 12345678  # <-- अपना MT5 Login ID डालें
password = "your_password"  # <-- पासवर्ड डालें
server = "YourBroker-Server"  # <-- ब्रोकरेज का सर्वर नाम

# Initialize
if not mt5.initialize(login=login, password=password, server=server):
    print("MT5 init failed:", mt5.last_error())
    quit()

symbol = "XAUUSD"
lot = 0.01
sl_pips = 50
tp_pips = 100

def place_trade():
    price = mt5.symbol_info_tick(symbol).ask
    sl = price - sl_pips * 0.1
    tp = price + tp_pips * 0.1

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": 10,
        "magic": 123456,
        "comment": "AutoBot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    print(f"[{datetime.now()}] Trade Result:", result)

# Run loop
while True:
    place_trade()
    sleep(3600)  # हर घंटे एक trade
