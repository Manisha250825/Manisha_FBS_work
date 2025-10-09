amount = int(input("Enter the amount in rupees: "))
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
note_count = {}
for note in denominations:
    count = amount // note
    if count > 0:
        note_count[note] = count
        amount %= note
print("Minimum number of notes needed:")
for note, count in note_count.items():
    print(f"₹{note} x {count}")