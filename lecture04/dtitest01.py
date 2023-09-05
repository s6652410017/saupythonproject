width = float (input("ป้อนความกว้าง :"))
long = float (input("ป้อนความยาว :"))
high = float (input("ป้อนความสูง :"))
print("---------------------------")
#คำนวณ
total_area = ((width*long) * 2) +  ((width*high) * 2) + ((high*long) * 2)
กี่แกลอน = round(total_area / 5)
print(f"you should have {long} long {width} widht and {high} tall should have {กี่แกลอน} gallon")
print("you should have" , long, "long" , width, "widht and" , high, "tall should have ",กี่แกลอน, "gallon")
print("you should hav" +str (long) + "long" +str (width) , "widht and "+str (high) + "tall should have" +str(กี่แกลอน))
print("you should have {} long {} width and {} gallon" .format ((long) , (width) , (high), (กี่แกลอน)))

