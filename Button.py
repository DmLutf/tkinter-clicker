import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

pointsPerSecond = 0
pointsPerClick = 1
totalScore = 0
totalClicks = 0
upgrade1Cost = 5
upgrade2Cost = 10


def click():
    global totalScore, totalClicks, pointsPerClick
    totalScore += pointsPerClick
    totalClicks += 1
    scoreCounter["text"] = "Score: " + str(totalScore)
    clickCounter["text"] = "Clicks: " + str(totalClicks)


def auto_click():
    global totalScore, pointsPerSecond
    totalScore += pointsPerSecond
    scoreCounter["text"] = "Score: " + str(totalScore)
    root.after(1000, auto_click)


def upgrade1():
    global pointsPerClick, totalScore, upgrade1Cost

    if totalScore >= upgrade1Cost:
        totalScore -= upgrade1Cost
        upgrade1Cost += 5
        pointsPerClick += 1

        scoreCounter["text"] = "Score: " + str(totalScore)
        upgrade1Button["text"] = "Upgrade(" + str(upgrade1Cost) + ")\n(per click)"
        perClickCounter["text"] = "+ " + str(pointsPerClick) + " points per click"


def upgrade2():
    global pointsPerSecond, totalScore, upgrade2Cost

    if totalScore >= upgrade2Cost:
        totalScore -= upgrade2Cost
        upgrade2Cost += 10
        pointsPerSecond += 1

        scoreCounter["text"] = "Score: " + str(totalScore)
        upgrade2Button["text"] = "Upgrade(" + str(upgrade2Cost) + ")\n(per second)"
        perSecondCounter["text"] = "+ " + str(pointsPerSecond) + " points per second"


scoreCounter = tk.Label(root, text="Score: " + str(totalScore),
                        font=("Courier New", 16, "bold"))
clickCounter = tk.Label(root, text="Clicks: " + str(totalClicks),
                        font=("Courier New", 16, "bold"))
perSecondCounter = tk.Label(root, text="+ " + str(pointsPerSecond) + " points per second")
perClickCounter = tk.Label(root, text="+ " + str(pointsPerClick) + " points per click")

mainButton = tk.Button(root, text="Click me", command=click,
                       bg="gray", activebackground="gray")
upgrade1Button = tk.Button(root, text="Upgrade(" + str(upgrade1Cost) + ")\n(per click)",
                           command=upgrade1, bg="gray",
                           activebackground="gray")
upgrade2Button = tk.Button(root, text="Upgrade(" + str(upgrade2Cost) + ")\n(per second)",
                           command=upgrade2, bg="gray",
                           activebackground="gray")

perClickCounter.place(x=147, y=125)
perSecondCounter.place(x=280, y=125)
scoreCounter.pack()
clickCounter.pack()

mainButton.place(height=100, width=100,
                 x=10, y=100)
upgrade1Button.place(height=50, width=100,
                     x=150, y=150)
upgrade2Button.place(height=50, width=100,
                     x=290, y=150)

auto_click()

root.mainloop()
