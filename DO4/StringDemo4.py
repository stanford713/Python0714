report='台積電目前價格每股300元,非常適合買進'
amount=1000
price=report[report.find('股')+1:report.find('元')]
print(price)
cost=amount*int(price)
print(cost)