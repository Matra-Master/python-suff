""" Mad Lib Generator
This should take a series of words from the user and print them
as a complete text.
"""

# something = "ElJuego"   # Some String variable
#
# print("Perdiste " + something)
# print("Perdiste {}".format(something))
# print(f"Perdiste {something}")

subj = input("Noun: ")
adj = input("Adjectibe: ")
verb1 = input("Verb: ")
obj1 = input("Object: ")
aname = input("Some Awesome name: ")
madlib = f"In medieval mithology, {subj} created the universe and it was {adj}! Then they \
{verb1} a {obj1} and called it {aname}"

print(madlib)
