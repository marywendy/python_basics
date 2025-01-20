W = 2000
F = 1200
SF = 720

tournaments = int(input())
initial_points = int(input())

final_points = initial_points
wins = 0

for _ in range(tournaments):
    tournament_stage = input()
    if tournament_stage == "W":
        final_points += W
        wins += 1
    elif tournament_stage == "F":
        final_points += F
    elif tournament_stage == "SF":
        final_points += SF

average_points = (final_points - initial_points) /tournaments
percentage_wins = wins / tournaments * 100

print(f"Final points: {final_points}\n"
      f"Average points: {int(average_points)}\n"
      f"{percentage_wins:.2f}%")