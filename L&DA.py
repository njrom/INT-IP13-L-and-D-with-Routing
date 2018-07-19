
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




def test():
    click(Pattern("Ultrasound.png").targetOffset(25, 0))
    type("m-5" + Key.TAB)
    type("17w 1d" + Key.TAB)
    keyDown(KeyModifier.SHIFT)
    type(Key.TAB)
    keyUp(KeyModifier.SHIFT)
    type(Key.ENTER) # Fancy way to select the radio button, hard to click that specific one otherwise

    if not exists("Working.png"):
        popup("Test Script failed Working did not appear")
        sys.exit("Test Script failed Working did not appear")

    click("ReCalculateDating.png")
    click("Recalculate.png")
    click("Close.png")
    





test()