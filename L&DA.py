
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

    click("Results Console.png")
    wait(2)
    type("M - 8" + Key.TAB)
    type("N" + Key.TAB)
    type("Krusch" + Key.TAB)
    type("External Lab")
    click("Comment.png")
    type("Lab Address here")
    click("Accept2.png")
    click(Pattern("ABO.png").targetOffset(-25, 0))
    type("O pos" + Key.ENTER)

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

    hover("Arrow.png")
    wait(4)
    click("Review PTA Meds.png")

    click("Prior to Admission Med.png")
    type(114929 + Key.ENTER)
    click("Database Lookup.png")
    type(Key.ENTER)

    click("Today.png")
    type("7 am")

    click("Med List Status.png")
    type("Up-To-Date.png" + Key.ENTER)
    type(Key.PAGE_DOWN)
    click("Mark as Reviewed.png")
    click("Close.png")


def test():
    click("NST Procedure.png")
    wait(2)
    click("Fetal nonstress.png")

    click(Pattern("Pre Procedure Diagnosis.png").targetOffset(250, 0))
    type("Decreased fetal movements [483632]"+Key.TAB+Key.ENTER)
    type(Key.TAB+ "047"+Key.TAB+Key.ENTER)
    click(Pattern("Singleton.png").targetOffset(-30, 0))
    click(Pattern("Now Start Time.png").targetOffset(140, 0))
    click("No.png")
    click("rare.png")
    click("absent.png")
    click(Pattern("FHR Baseline.png").targetOffset(200, 0))
    type("123")
    click(Pattern("Decelerations none.png").targetOffset(65, 0))
    click(Pattern("Accelerations none.png").targetOffset(65, 0))
    click("Acoustic.png")
    click("Nonreactive.png")
    click(Pattern("Now End Time.png").targetOffset(140, 0))
    click("Paper.png")

    type(Key.TAB + "Resident"+ Key.TAB)
    type("Suggest Repeat NST in 24 hours"+Key.ENTER)
    type(Key.TAB*2 + "T + 1 ")

    click(Pattern("Date of Service.png").targetOffset(60, 0))
    type("T"+Key.TAB)
    type("N"+Key.TAB)
    type("URMC OBSTETRICS, PHYSICIAN"+Key.TAB)

    type(Key.F2)
    type("Y" +Key.ENTER)
    type(Key.F2)
    type("Y" + Key.ENTER)
    type(Key.F2)
    type("Y" + Key.ENTER)
    type(Key.F2)
    type("Y" + Key.ENTER)
    type(Key.F2)
    type("Y" + Key.ENTER)
    type(Key.F2)
    type("Y" + Key.ENTER)
    type(Key.F2)
    type("Y" + Key.ENTER)

    if not exists("Note Verification.png") :
        popup("Script failed smart form text does not reflect the info entered")
        sys.exit("Script failed smart form text does not reflect the info entered")

    click("Sign.png")









    





test()