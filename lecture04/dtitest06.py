ฃื่อ_product = input("ใส่ฃื่อ product")
budget = float(input("ใส่ budget product"))

def productVAlue(budget):
    product_ราคาจริง = budget + (budget * 10/100)
    return "%.2f" % product_ราคาจริง

print(f"ราคาของ {ฃื่อ_product} คือ {productVAlue(budget)}")
