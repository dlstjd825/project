import httpx

def get_user_info(handle: str):
    # API URL
    api_url = f"https://solved.ac/api/v3/user/show?handle={handle}"
    
    # HTTP 요청
    try:
        response = httpx.get(api_url)
        if response.status_code == 200:
            user_info = response.json()
            
            # 티어 숫자를 가져옴
            tier_number = user_info['tier']
            
            # 티어 매핑
            tier_mapping = {
                1: "Bronze V", 2: "Bronze IV", 3: "Bronze III", 4: "Bronze II", 5: "Bronze I",
                6: "Silver V", 7: "Silver IV", 8: "Silver III", 9: "Silver II", 10: "Silver I",
                11: "Gold V", 12: "Gold IV", 13: "Gold III", 14: "Gold II", 15: "Gold I",
                16: "Platinum V", 17: "Platinum IV", 18: "Platinum III", 19: "Platinum II", 20: "Platinum I",
                21: "Diamond V", 22: "Diamond IV", 23: "Diamond III", 24: "Diamond II", 25: "Diamond I",
                26: "Ruby V", 27: "Ruby IV", 28: "Ruby III", 29: "Ruby II", 30: "Ruby I",
                31: "Challenger"
            }
            
            # 사람이 읽을 수 있는 티어로 변환
            tier_name = tier_mapping.get(tier_number, "Unknown")
            
            # 점수 정보 가져오기
            rating = user_info.get('rating', 0)
            
            return {
                "handle": handle,
                "tier": tier_name,
                "rating": rating,
                "now_tier":tier_number,
            }
        else:
            return {"error": f"Failed to fetch data: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}