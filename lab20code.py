#!/usr/bin/env python3
# Alta3 | Lab 20 code

#import random module

import random

def main():

    wordbank= ["indentation", "spaces"]
    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

    print(tlgstudents)

    wordbank.append(4)
    print(wordbank)

    num = int(input(f"Enter a student number between 1 and {len(tlgstudents)} --> "))-1
    name = tlgstudents[num]

    print(f"Your unfortunate victim is {name}!")

    print (f"{name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    name = random.choice(tlgstudents)
    print(f"{name}")

if __name__ == "__main__":
    main()


