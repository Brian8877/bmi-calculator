height = float(input("請輸入身高(公分):"))/100
weight = float(input("請輸入體重(公斤):"))
bmi = weight/(height**2)
print(f"你的bmi為:{bmi:.2f}")
if bmi<18.5:
  print("過輕")
elif bmi<24:
  print("正常")
elif bmi<27:
  print("過重")
else:
  print("肥胖")
