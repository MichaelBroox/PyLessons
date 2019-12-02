subtotal = float(input('Enter subtotal value: \n>>> '))
gratuity = float(input('Enter gratuity rate value: \n>>> '))

new_gra = gratuity / 100
new_sub = subtotal + new_gra

print('The gratuity rate value you entered was {} \nAnd the new gratuity rate value is {}'.format(gratuity, new_gra))
print('The subtotal value you entered was {} \nAnd the new subtotal value is {}'.format(subtotal, new_sub))
