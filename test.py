import pyupbit

access = "AjbPHzj993dQM9Y0Rnv5QAvK6n4It2lI0cMLa4Bv"          # 본인 값으로 변경
secret = "qTECHP2K3su9VKZl6cXqlbiTg09xSOQblphcyixx"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("DOGE"))     # KRW-DOGE 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회