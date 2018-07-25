
from lackey import *
import sys



def main():
    click("In Basket.png")
    click("Cosign Notes.png")
    wait(1)
    if exists("NST Verification.png"):
        click("NST Verification.png")
        click("Cosign.png")
    else:
        popup("Select your Order and hit Cosign")

    click("L&D Grease Board.png")
    click("314.png")
    popup("Double Click on the results icon")



main()