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

self.keyboard.walk("d", 3)
self.keyboard.walk("s", 0.5)

while True:
    # Check if defeated
    if self.blueTextImageSearch("defeated") and self.blueTextImageSearch("tunnelbear"):
        break
    # Check if died
    if self.blueTextImageSearch("died"):
        self.died = True
        break
    # Continue the movement pattern
    self.keyboard.walk("d", 0.25)
    sleep(1)
sleep(1)
# Collect rewards
self.keyboard.walk("d", 1.5)
self.keyboard.walk("a", 3)