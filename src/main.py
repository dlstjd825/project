from make_profile import generate_profile_card

handle = input("BOJ아이디 입력 > ")
print()

print("------------ 옵션 ------------")
print("| 1. 카드 저장만 하기        |")
print("| 2. 카드 확인 & 저장하기    |")
print("| 3. 종료                    |")
print("------------------------------")

while True:
    try:
        opt_input = input("옵션 선택 > ")
        opt = int(opt_input)
        if opt < 1 or opt > 3:
            raise ValueError("1, 2, 3 중 하나를 입력하세요.")
        break
    except ValueError:
        if not opt_input.isdigit():
            print("잘못된 입력입니다. 숫자를 입력하세요.")
        else:
            print("1, 2, 3 중 하나를 입력하세요.")
    except Exception:
        print("예기치 못한 오류가 발생했습니다.")


if (opt==3):
    exit(0)

print("잠시 기다려 주세요!")
generate_profile_card(handle, opt)

