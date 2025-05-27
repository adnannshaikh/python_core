is_magician = False
is_expert = True

# Check if the magician and expert :
if is_magician and is_expert:
    print("You are a Master Magician")
# Check if magician but not expert:
elif is_magician and not is_expert:
    print("At least you're getting there")
# If you're not a magician:
elif not is_magician:
    print("You need magical powers")