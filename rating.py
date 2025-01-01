from api import get_user_info

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

def get_ratings_progress(handle: str):
    user_info = get_user_info(handle)
    idx = user_info['now_tier']
    
    if idx!=31:
        prev_rating = TIER_RATES[idx]
        next_rating = TIER_RATES[idx+1]
        
        gap = next_rating - prev_rating
        current = user_info['rating'] - prev_rating
        
        now_rating = f"{user_info['rating']:,} / {next_rating:,}"
        
        progress = int(round(current * 100 / gap,0))
    else:
        # 마스터는 따로 처리
        now_rating = f"{user_info['rating']:,}"
        progress = 100
    
    return now_rating, progress
