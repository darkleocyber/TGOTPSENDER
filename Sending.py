import TgOtpsent
import inspect

print("Module loaded:", TgOtpsent.__name__)

if hasattr(TgOtpsent, "auto_run"):
    try:
        print("Auto_run arguments:", inspect.signature(TgOtpsent.auto_run))
    except (ValueError, TypeError):
        print("Signature not available.")
elif hasattr(TgOtpsent, "main"):
    try:
        print("Main arguments:", inspect.signature(TgOtpsent.main))
    except (ValueError, TypeError):
        print("Main signature not available.")
else:
    print("No auto_run or main function found.")

print("Available functions:")
print([name for name in dir(TgOtpsent) if not name.startswith("_")])
