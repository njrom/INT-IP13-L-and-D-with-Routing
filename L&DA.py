
from lackey import *
import sys


def main():
    App.focus("URMC POC")
    click("TriageAdmit.png")
    click("OB Arrival Info.png")
    click("Singleton.png")
    click("BreastFeeding.png")
    click("Requested.png")
    click("Next.png")

    click("NotApplicable.png")

    click("ChiefComplaint.png")
    type("Laboring"+Key.ENTER)
    type(Key.ENTER)
    click("Close.png")

    click("Dating.png")

    click(Pattern("Ultrasound.png").targetOffset(25, 0))
    type("m-5" + Key.TAB)
    type("17w 1d" + Key.TAB)
    keyDown(KeyModifier.SHIFT)
    type(Key.TAB)
    keyUp(KeyModifier.SHIFT)
    type(Key.ENTER)  # Fancy way to select the radio button, hard to click that specific one otherwise

    if not exists("Working.png"):
        popup("Test Script failed Working did not appear")
        sys.exit("Test Script failed Working did not appear")

    click("ReCalculateDating.png")
    click("Recalculate.png")
    click("Close.png")


def test():
    click("Results Console.png")
    wait(2)
    type("M - 8"+Key.TAB)
    type("N"+Key.TAB)
    type("Krusch"+Key.TAB)
    type("External Lab")
    click("Comment.png")
    type("Lab Address here")
    click("Accept2.png")
    click(Pattern("ABO.png").targetOffset(-25, 0))
    type("O pos"+Key.ENTER)

    click(Pattern("Antibody.png").targetOffset(-30, 0))
    type("neg")

    click(Pattern("Rubella.png").targetOffset(-24, 0))
    type("neg")

    click(Pattern("Result Date.png").targetOffset(40, 0))
    type("m - 5")

    # 1 hour gluecose tolerance = 95
    # Required section HCT = 39  accept and close
    click(Pattern("1hr Glucose Tolerance.png").targetOffset(-80, 0))
    type("95")

    click("Close.png")

    click("Save.png")


    





test()