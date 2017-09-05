def getFizzBuzzList(multiples, *args):
    for i in range(*args):
        output = ''
        for multiple in multiples:
            if i % multiple==0:
                output+=multiples[multiple]
        if output =='':
            output = i
        print(output)

multiples = {3:'Fizz',5:'Buzz'}
getFizzBuzzList(multiples,101)
