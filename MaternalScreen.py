
from lackey import *
from Patients import Patients
import sys


USERNAME = "ADTADM"
DEPARTMENT = "SMH Admitting"
PATIENT_NUMBER = 1  # This is the number that dictates the patient name, if the patient exists already, raise it


def main():
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
    click("SelectEDDRadioButton.png")
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
    click(Pattern("Maternal1stTrimesterScreen.png").targetOffset(-110, 0))









main()