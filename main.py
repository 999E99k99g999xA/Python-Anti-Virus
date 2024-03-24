from AntiVirus import AntiVirus
from GUI import AppGUI


v = AntiVirus(None)
a = AppGUI(v)
v.GUI = a
a.displayWindow()