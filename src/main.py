from make_profile import generate_profile_card
from api import get_user_info

# 테스트
handle = input("input your BOJ id > ")
info = get_user_info(handle)

print(info)

generate_profile_card(handle)

