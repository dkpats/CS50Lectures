# Create an empty set
s = set()

# Add elements to the set 's'

s.add(2)
s.add(9)
s.add(4)
s.add(2)

print(s)
print(f"The set has {len(s)} elements.")

s.remove(2)

print(s)
print(f"The set now has {len(s)} elements.")
print(f"The 1st element length is {len(s[0])}.")
