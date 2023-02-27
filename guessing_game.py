secret_word = 'muhamed'
guess = ''
counter = 0
limit = 3
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if counter <= limit:
        guess = input('enter guess')
        counter += 1
    else:
        out_of_guess = True
if out_of_guess:
    print('you lost!!')
else:
    print('you win')


