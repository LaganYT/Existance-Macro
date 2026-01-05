# Navigate to honey storm location and summon it
self.runPath("collect/stockings")
self.keyboard.walk("a",1.25, False)
self.keyboard.walk("s",1.5)
self.keyboard.walk("d",0.45)
self.keyboard.walk("s",0.7)
sleep(1)
self.keyboard.press("e")


self.keyboard.walk("s", 3)
self.keyboard.walk("d", 2)

for i in range(8):
    self.keyboard.walk("w", 2.25)
    self.keyboard.walk("d", 0.25)
    self.keyboard.walk("s", 2.25)
    self.keyboard.walk("d", 0.25)
sleep(0.5)
#credit to laganyt for the path