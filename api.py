import httpx

TIERS = (
    "Unrated",
    "Bronze 5", "Bronze 4", "Bronze 3", "Bronze 2", "Bronze 1",
    "Silver 5", "Silver 4", "Silver 3", "Silver 2", "Silver 1",
    "Gold 5", "Gold 4", "Gold 3", "Gold 2", "Gold 1",
    "Platinum 5", "Platinum 4", "Platinum 3", "Platinum 2", "Platinum 1",
    "Diamond 5", "Diamond 4", "Diamond 3", "Diamond 2", "Diamond 1",
    "Ruby 5", "Ruby 4", "Ruby 3", "Ruby 2", "Ruby 1",
    "Master"
)

def get_user_info(handle: str):
    # API URL
    api_url = f"https://solved.ac/api/v3/user/show?handle={handle}"
    
    # HTTP 요청
    try:
        response = httpx.get(api_url)
        if response.status_code == 200:
            user_info = response.json()
            
            # 티어 인덱스 가져오기
            tier_idx = user_info['tier']
            
            # 사람이 읽을 수 있는 티어로 변환
            tier_name = TIERS[tier_idx]
            
            # 점수 정보 가져오기
            rating = user_info.get('rating', 0)
            
            # 맞은 문제 수 가져오기
            solved_count = user_info.get('solvedCount', 0)
            
            # 클래스 정보 가져오기
            user_class = user_info.get('class', 0)
            
            # 프로필사진 url
            profile_image_url = user_info.get('profileImageUrl', None)
            
            return {
                "handle": handle,
                "tier": tier_name,
                "rating": rating,
                "now_tier":tier_idx,
                "solved":solved_count,
                "class":user_class,
                "profile_image":profile_image_url,
            }
        else:
            return {"error": f"Failed to fetch data: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}