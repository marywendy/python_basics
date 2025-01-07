YEARLY_PLAY_NORM = 30000
DAILY_PLAY_WORK_DAYS = 63
DAILY_PLAY_REST_DAYS = 127

rest_days = int(input())

rest_day_play = rest_days * 127
work_day_play = (365 - rest_days) * 63
yearly_play = rest_day_play + work_day_play

difference_from_norm = YEARLY_PLAY_NORM - yearly_play

hours = abs(difference_from_norm) // 60
minutes = abs(difference_from_norm) % 60

if difference_from_norm < 0:
    print(f'Tom will run away\n{hours} hours '
          f'and {minutes} minutes more for play')
elif difference_from_norm > 0:
    print(f'Tom sleeps well\n{hours} hours '
          f'and {minutes} minutes less for play')

