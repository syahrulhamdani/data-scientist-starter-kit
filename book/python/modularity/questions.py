from choices import fastfood, advice

place = fastfood.pick()
take_out = advice.give()

print("Let's go to {} for lunch!".format(place))
print("Should we take out?", take_out)
