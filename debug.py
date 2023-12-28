import time

from pywinauto import Application

app = Application(backend="uia").start(fr"calc.exe")
#time.sleep(3)

app.connect(best_match="Calculator", timeout=5)
numbut = app.top_window().child_window(class_name="NamedContainerAutomationPeer", found_index=4)
numbut.draw_outline()
time.sleep(3)
app.kill()
