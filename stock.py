stock = [(20,5.50),(15,8.30),(37,3.85),(4,11.60)]
total_value = sum(map(lambda product: product[0] * product[1], stock))
#map applies lambda to each product (element) in stock
print(f'Products in stock:: {stock}')
print(f'Total value: {total_value}')