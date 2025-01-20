number_of_groups = int(input())

group_musala = 0
group_montblanc = 0
group_kilimanjaro = 0
group_k2 = 0
group_everest = 0

for _ in range(number_of_groups):
    people_in_group = int(input())
    if  1 <= people_in_group <= 5:
        group_musala += people_in_group
    elif 5 < people_in_group <= 12:
        group_montblanc += people_in_group
    elif 12 < people_in_group <= 25:
        group_kilimanjaro += people_in_group
    elif 25 < people_in_group <= 40:
        group_k2 += people_in_group
    elif people_in_group > 40:
        group_everest += people_in_group

people_total = group_musala + group_montblanc + group_kilimanjaro + group_k2 + group_everest

percent1 = group_musala / people_total * 100
percent2 = group_montblanc / people_total * 100
percent3 = group_kilimanjaro / people_total * 100
percent4 = group_k2 / people_total * 100
percent5 = group_everest / people_total * 100

print(f"{percent1:.2f}%\n"
      f"{percent2:.2f}%\n"
      f"{percent3:.2f}%\n"
      f"{percent4:.2f}%\n"
      f"{percent5:.2f}%")