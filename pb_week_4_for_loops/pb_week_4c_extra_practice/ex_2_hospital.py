DOCTORS = 7

days = int(input())

examined_patients = 0
unexamined_patients = 0

for d in range(1, days + 1):
    incoming_patients = int(input())

    if d % 3 == 0 and unexamined_patients > examined_patients:
        DOCTORS += 1

    if DOCTORS >= incoming_patients:
        examined_patients += incoming_patients
    else:
        examined_patients += DOCTORS
        unexamined_patients += incoming_patients - DOCTORS

print(f"Treated patients: {examined_patients}.\n"
      f"Untreated patients: {unexamined_patients}.")
