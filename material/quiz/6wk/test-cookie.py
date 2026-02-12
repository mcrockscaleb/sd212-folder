# Sample testing code for the cookie jar problem
# You can modify this if you want; it will not be submitted.

from cookie import CookieJar

# Setup two different jars
bert = CookieJar("Bert", 10)
ernie = CookieJar("Ernie", 20)

print(bert)
print(ernie)

# Steal from Bert
bert.steal(2)
print(bert)
print(f"Monster has {bert.total_stolen()} cookies")

# Steal from Ernie (Should update the SAME global counter)
ernie.steal(5)
print(ernie)
print(f"Monster has {ernie.total_stolen()} cookies")

# Steal from Bert AGAIN
bert.steal(3)
print(bert)
print(f"Monster has {bert.total_stolen()} cookies")
