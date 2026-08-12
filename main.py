import time
ch = ""
def timer(t):
    while t > 0:
        m, s = divmod(t, 60)
        timer = f"{m:02d}:{s:02d}"
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Time's up!")
print("Hello, that's program help you level up your skills (like sport, music and other stuff) Only what you should do, just do it your regular tasks, solet's start! (if you eant to leave program, just wrote [exit], when you choising skills)")
while ch != "exit":
    print("1. Music\n2. Sport\n3. Reading")
    ch = str(input("Enter number of Skill: "))
    if ch == "1":
        print("Play on your today instrument, about 30 minutes\nTimer:")
        print(timer(int(1800)))
        print("Congratulations, task complete! Backing to menu...")
    if ch == "2":
        print("Make 30 push-ups, 50 squads and 100 crunches\nIf you done, write [that's be very hard, but I'm done]")
        d = str(input("Ready? >> "))
        print("Congratulations, task complete! Backing to menu...")
    if ch == "3":
        print("Sorry, tasks aren't done yet. Backing to menu... ")
