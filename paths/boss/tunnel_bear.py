self.keyboard.walk("s", 7)
self.keyboard.walk("d", 2)
self.keyboard.walk("s", 2)
self.keyboard.walk("a", 0.25)
self.keyboard.press(" ")
self.keyboard.walk("w", 0.5)
sleep(0.5)
self.keyboard.press(" ")
self.keyboard.walk("a", 0.5)
sleep(1)

self.keyboard.walk("d", 3.5)
self.keyboard.walk("s", 0.5)

# Continue the movement pattern while boss monitoring happens in background thread
while self.bossStatus is None and not self.died:
    self.keyboard.walk("d", 0.25)
    sleep(0.75)
# Collect rewards if defeated
if self.bossStatus == "defeated":
    self.keyboard.walk("d", 1.5)
    self.keyboard.walk("a", 3)
    sleep(1)