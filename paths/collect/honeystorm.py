# Navigate to honey storm location and summon it
self.runPath("collect/stockings")
self.keyboard.walk("a",1.25, False)
self.keyboard.walk("s",1.5)
self.keyboard.walk("d",0.45)
self.keyboard.walk("s",0.4)
self.keyboard.walk("a", 0.45)
for slowmove in range(9):
    self.keyboard.walk("d", 0.048, False) #move JUST EVER SO SLIGHTLY, maybe bumps in to wall less
    time.sleep(0.035)
self.keyboard.press("e")
time.sleep(1.5)
