import importlib.util
import sys

# ফাইলের সঠিক পাথ দিন (Termux-এ আপনার প্রজেক্ট ফোল্ডারের পাথ অনুযায়ী পরিবর্তন করুন)
file_path = "/data/data/com.termux/files/home/TGOTPSENDER/TGOTPSENDER/TgOtpsent.cpython-311.pyc" # এখানে আপনার ফাইলের নাম দিন

spec = importlib.util.spec_from_file_location("TgOtpsent", file_path)
TgOtpsent = importlib.util.module_from_spec(spec)
sys.modules["TgOtpsent"] = TgOtpsent
spec.loader.exec_module(TgOtpsent)

# এখন চেক করুন TgOtpsent-এ কী কী ফাংশন আছে
print([name for name in dir(TgOtpsent) if not name.startswith("_")])
