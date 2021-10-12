def get_result(number):
    def is_divisible(divisor):
        return number % divisor == 0

    def create_rule(name, validityCondition):
        return {'name': name, 'isValid': validityCondition}

    rules = [
        create_rule('Fizz', is_divisible(3) and not is_divisible(11)),
        create_rule('Fezz', is_divisible(13)),
        create_rule('Buzz', is_divisible(5) and not is_divisible(11)),
        create_rule('Bang', is_divisible(7) and not is_divisible(11)),
        create_rule('Bong', is_divisible(11)),
    ]

    resultWords = []

    for rule in rules:
        if rule['isValid']:
            resultWords.append(rule['name'])

    if is_divisible(17):
        resultWords.reverse()

    if resultWords == []:
        return str(number)
    else:
        return ''.join(resultWords)


for number in range(1,144):
    print(get_result(number))
    