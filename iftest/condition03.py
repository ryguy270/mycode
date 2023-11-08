#!/usr/bin/env python3
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if (input("What value should we set for hostname?"))() == "mtg":
    print("The hostname was found to be mtg")
if (input("What value should we set for hostname?"))() == "MTG":
    print("The hostname was found to be something crazy")
    