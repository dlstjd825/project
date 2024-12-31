from api import get_user_info
from rating import get_ratings_progress

TIER_RATES = (
    0, # unranked
    30, 60, 90, 120, 150, # bronze
    200, 300, 400, 500, 650, # silver
    800, 950, 1100, 1250, 1400, # gold
    1600, 1750, 1900, 2000, 2100, # platinum
    2200, 2300, 2400, 2500, 2600, # diamond
    2700, 2800, 2850, 2900, 2950, # ruby
    3000 # master
)

# 테스트
handle = input("input your boj id > ")
user_info = get_user_info(handle)

now_rating, progress = get_ratings_progress(handle)

print("ID :", handle)
print("Tier :", user_info['tier'])
print(f"Rating : {now_rating}")
print("Progress :", str(progress)+'%')