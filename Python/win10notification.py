# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Notificações no Windows 10 ---
from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("JJEAN_DEV", "Hello world 😎", duration=10)
