
from lackey import *
import sys


def main():
    App.focus("URMC POC")
    click("OB Triage.png")
    wait(1)
    click("Allergies.png")
    wait(1)
    click("NoKnownAllergies.png")
    click("MarkAsReviewed.png")
    click("Episodes.png")
    if not exists("PregnancyEpisode.png"):
        popup("Pregnancy Episode is not Present")
        sys.exit("Pregnancy Episode not Present")
    click("Dating.png")
    wait(2)
    click("LastMenstrualPeriod.png")
    type("T-60"+Key.ENTER)
    click(Pattern("RadioButton.png").targetOffset(246, 0))
    click("ReCalculateDating.png")
    wait(2)
    click("Recalculate.png")
    click("Close.png")
    wait(1)
    click("ManageOrders.png")
    type("Maternal Screen"+Key.ENTER)
    wait(1)
    type(Key.ENTER)
    wait(1)

    click(Pattern("Maternal1stTrimesterScreen.png").targetOffset(-108, 0))
    wait(1)
    ans = popAsk("Are the collection date ranges present ?")
    if not ans:
        sys.exit("Script Failed Dates are not contained")

    click("Cancel.png")

    click(Pattern("Maternal2ndTrimesterScreen.png").targetOffset(-108, 0))
    wait(1)
    ans = popAsk("Are the collection date ranges present ?")
    if not ans:
        sys.exit("Script Failed Dates are not contained")

    click("Cancel.png")

    click(Pattern("MaternalAFPOnly.png").targetOffset(-65, 0))
    wait(1)
    type(Key.PAGE_DOWN)
    ans = popAsk("Are the collection date ranges present?")
    if not ans:
        sys.exit("Script Failed Dates are not contained")

    click(Pattern("IVFQuestion.png").targetOffset(100,
                                                  0))  # Tip: use Snaggit to find distance in points from center to where you need to click

    if exists("EggSourceQuestion.png"):
        popup("Script failed Egg Source Question appeared")
        sys.exit("Script failed Egg Source Question appeared")

    click(Pattern("IVFQuestionV2.png").targetOffset(54, 0))
    wait(1)

    if not exists("EggSourceQuestion.png"):
        popup("Script failed Egg Source Question did not appear")
        sys.exit("Script failed Egg Source Question did not apper")

    type(Key.PAGE_UP)
    click("Cancel.png")

    click("Accept.png")
    click("DiscardChanges.png")
    click("X.png")
    popup("Script functioned properly.")




main()