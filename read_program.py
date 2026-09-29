import csv

with open("week1.csv", newline="", encoding="utf-8") as file:
    program = list(csv.DictReader(file))

for exercise in program:
    print(
        exercise["session"],
        exercise["exercise"],
        f'{exercise["sets"]} x {exercise["reps"]}',
        exercise["target"],
    )
    session_reps = {}

for exercise in program:
    session = exercise["session"]
    reps = int(exercise["sets"]) * int(exercise["reps"])
    session_reps[session] = session_reps.get(session, 0) + reps

print("\nTotal prescribed reps per session:")
for session, total_reps in session_reps.items():
    print(f"{session}: {total_reps}")