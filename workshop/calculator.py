import math

allowed_operators = {'/','x','+','-','%'}

def parse_calculation (parameter_list):

    if len(parameter_list) != 3:
        print('Incorrect number of values entered')
        return False

    if parameter_list[0] not in allowed_operators:
        print('Invalid operator')
        return False
    
    try:
        return (parameter_list[0], int(parameter_list[1]), int(parameter_list[2]))
    except:
        print('Invalid values used in calculation')
        return False

def execute_calculation(parsed_calculation):
    operator = parsed_calculation[0]
    first_num = parsed_calculation[1]
    second_num = parsed_calculation[2]
    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case 'x':
            return first_num * second_num
        case '/':
            return first_num / second_num
        case '%':
            return first_num % second_num

def handle_calculation(calc):
    return execute_calculation(parse_calculation(calc))

# STEP 1
# while True:
#     command = input('Enter a calculation or "quit": ')
#     if command == 'quit':
#         break
    
#     parsed_command = parse_command(command.split())

#     if parsed_command == False:
#         continue

#     print(execute_command(parsed_command))

def parse_command(command):
    command_parameters = command.split()
    return (command_parameters[0], command_parameters[1:])

with open('s2_input.txt', 'r') as f:
    raw_commands = f.read().splitlines()
    results = []

    for raw_command in raw_commands:
        try:
            command = parse_command(raw_command)
            calculation = parse_calculation(command[1])
            result = execute_calculation(calculation)
            results.append(result)
        except:
            print('ERROR: command {c} failed'.format(c = raw_command))
    
    sum = 0.0

    for result in results:
        sum += result

    print('step 2:')
    print(sum)

def execute_command(raw_command):
    command = parse_command(raw_command)
    match command[0]:
        case 'calc':
            return math.floor(handle_calculation(command[1]))
        case 'goto':
            if len(command[1]) == 1:
                position = command[1][0]
                return int(position)
            else:
                inner_command = ' '.join(command[1])
                return execute_command(inner_command)

    
with open('s3_input.txt', 'r') as f:
    raw_commands = f.read().splitlines()
    seen_commands = set()

    active_command = raw_commands[0]
    active_line = 1
    while not active_command in seen_commands:
        try:
            seen_commands.add(active_command)
            active_line = execute_command(active_command)
            active_command = raw_commands[active_line - 1]
        except:
            print('ERROR: command {c} failed'.format(c = active_command))
            print(seen_commands)
            break
    
    print('step 3:')
    print('line: {l}'.format(l = active_line))
    print('command: {c}'.format(c = active_command))

def execute_command4(raw_command, all_commands, active_line):
    command = parse_command(raw_command)
    match command[0]:
        case 'calc':
            return math.floor(handle_calculation(command[1]))
        case 'goto':
            if len(command[1]) == 1:
                position = command[1][0]
                return int(position)
            else:
                inner_command = ' '.join(command[1])
                return execute_command(inner_command)
        case 'remove':
            remove_line = int(command[1][0])
            if len(all_commands) >= remove_line:
                del all_commands[remove_line - 1]
            return active_line + 1
        case 'replace':
            replaced_line = int(command[1][0])
            replacing_line = int(command[1][1])
            if len(all_commands) >= replaced_line and len(all_commands) >= replacing_line:
                all_commands[replaced_line - 1] = all_commands[replacing_line - 1]
            return active_line + 1

with open('s4_input.txt', 'r') as f:
    raw_commands = f.read().splitlines()
    seen_commands = set()

    active_command = raw_commands[0]
    active_line = 1
    while not active_command in seen_commands:
        try:
            seen_commands.add(active_command)
            active_line = execute_command4(active_command, raw_commands, active_line)
            if active_line > len(raw_commands):
                break
            active_command = raw_commands[active_line - 1]
        except:
            print('ERROR: command {c} failed'.format(c = active_command))
            break
    
    print('step 4:')
    print('line: {l}'.format(l = active_line))
    print('command: {c}'.format(c = active_command))
    print(seen_commands)

