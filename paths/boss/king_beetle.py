# get into area
self.keyboard.keyDown("a")
sleep(1)
self.keyboard.keyUp("a")
self.keyboard.keyDown("w")
sleep(4)
self.keyboard.keyUp("w")
self.keyboard.keyDown("s")
sleep(0.95)
self.keyboard.keyUp("s")
self.keyboard.keyDown("d")
sleep(1.8)
self.keyboard.press("space")
self.keyboard.keyDown("s")
sleep(1)
self.keyboard.keyUp("s")
sleep(6)
self.keyboard.keyUp("d")
#back right corner
self.keyboard.keyDown("s")
sleep(5)
self.keyboard.keyUp("s")
start_time = time.time()
# Wait for king beetle to be defeated
while True:
    # Check for 3 minute timeout (180 seconds)
    if time.time() - start_time > 180:
        self.logger.webhook("", "King Beetle on cooldown", "dark brown", "screen")
        break

    # Check if defeated
    if self.blueTextImageSearch("kingbeetle", 0.8):
        # Collect rewards
        self.keyboard.walk("a", 1)
        self.keyboard.walk("w", 3)
        for i in range(3):
            self.keyboard.walk("a", 0.25)
            self.keyboard.walk("s", 2)
            self.keyboard.walk("a", 0.25)
            self.keyboard.walk("w", 2)
        sleep(1)
        self.saveTiming("king_beetle")
        break
    # Check if died
    if self.blueTextImageSearch("died"):
        self.died = True
        break
    # Small delay to prevent excessive CPU usage
    sleep(1)
sleep(1)
#credit to rubicorb.v2 for the path