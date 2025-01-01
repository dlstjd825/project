import httpx
import os
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps
from api import get_user_info
from rating import get_ratings_progress
import os

# 폴더 경로
folder = "profile"

# 폴더가 없으면 생성
if not os.path.exists(folder):
    os.makedirs(folder)

def generate_profile_card(handle: str):
    output_file = f"profile/{handle}_profile.png"
    
    # 사용자 정보 가져오기
    try:
        user_info = get_user_info(handle)
        tier = user_info['tier']
        rating = user_info['rating']
        solved = user_info['solved']
        user_class = user_info['class']
        profile_img_url = user_info['profile_image']
        now_rating, progress = get_ratings_progress(handle)
    except:
        tier = "Unknown"
        profile_img_url = None
            
    # 프사 없으면 기본 프사로 대체
    if profile_img_url == None:
        profile_img_url = r"https://i.namu.wiki/i/Bge3xnYd4kRe_IKbm2uqxlhQJij2SngwNssjpjaOyOqoRhQlNwLrR2ZiK-JWJ2b99RGcSxDaZ2UCI7fiv4IDDQ.webp"
    
    # 카드 크기와 설정
    card = Image.open(f"img/background/{tier.split()[0].lower()}.png").convert("RGBA")
    
    # 텍스트 이미지를 열기
    text_image = Image.open(f"img/text/{tier.split()[0]}.png")
    text_image_resized = text_image.resize((1011, 637))
    
    card.paste(text_image_resized, (0, 0), text_image_resized)  # text_image가 투명 배경일 경우, 세 번째 인수 추가
    
    # 프로필 이미지 추가
    profile_response = httpx.get(profile_img_url)
    profile_img = Image.open(BytesIO(profile_response.content)).resize((333, 333))
    profile_img = ImageOps.fit(profile_img, (333, 333), method=Image.Resampling.LANCZOS)
    mask = Image.new("L", (333, 333), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, 333, 333), fill=255)
    card.paste(profile_img, (75, 61), mask)
    
    if tier=='Unrated' or tier=='Unknown':
        card.save(output_file)
        print(f"Profile card saved as '{output_file}'")
        return 0
    
    font_handle = ImageFont.truetype("font/SpoqaHanSansNeo-Bold.ttf", 50)  # 핸들 폰트
    font_info = ImageFont.truetype("font/SpoqaHanSansNeo-Medium.ttf", 30)  # 기본 내용 폰트
    font_small = ImageFont.truetype("font/SpoqaHanSansNeo-Medium.ttf", 25)  # 작은 폰트
    
    # 텍스트용 객체
    draw = ImageDraw.Draw(card)
    draw.text((450, 70), handle, font=font_handle, fill=(255, 255, 255))        # 핸들
    draw.text((790, 163), tier, font=font_info, fill=(255, 255, 255))           # 티어
    draw.text((790, 235), f"{rating:,}", font=font_info, fill=(255, 255, 255))  # 레이팅
    draw.text((790, 305), f"{solved:,}", font=font_info, fill=(255, 255, 255))  # 푼문제수
    draw.text((790, 378), str(user_class), font=font_info, fill=(255, 255, 255))# 클래스
    draw.text((440, 492), now_rating, font=font_small, fill=(255, 255, 255))    # 현재레이팅/다음레이팅
    draw.text((910, 459), f"{progress}%", font=font_small, fill=(255, 255, 255))# 진행도
    
    # 진행도 막대
    overlay = Image.new("RGBA", card.size, (255, 255, 255, 0))  # 투명 레이어 생성
    draw = ImageDraw.Draw(overlay)
    
    bar_start = (440, 470)  # 바의 시작 좌표 (x, y)
    bar_end = (900, 480)   # 바의 끝 좌표 (x, y) (100% 길이 기준)
    bar_width = bar_end[0] - bar_start[0]
    
    current_length = int(bar_width * (progress / 100))
    draw.rectangle([bar_start, bar_end], fill=(255, 255, 255, 128))
    draw.rectangle([bar_start, (bar_start[0] + current_length, bar_end[1])], fill=(255, 255, 255, 255))

    card = Image.alpha_composite(card, overlay)
    
    card.save(output_file)
    print(f"Profile card saved as '{output_file}'")
    card.show()