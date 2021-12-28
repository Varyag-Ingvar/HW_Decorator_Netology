from datetime import datetime

log_file_path = 'log_some_func.txt'


def get_log(function):
    def new_function(*args, **kwargs):
        run_date_time = datetime.now()
        function_name = function.__name__
        result = function(*args, **kwargs)
        with open('log_some_func.txt', 'a', encoding='utf-8') as file:
            file.write(f'Function run Date-Time: {run_date_time}\n'
                       f'Function name: {function_name}\n'
                       f'Function arguments: {args, kwargs}\n'
                       f'Function execution result: {result}\n'
                       '-------------------------------------\n')
        return result
    return new_function


def get_log_1(parameter):
    def decor(function):
        def new_function(*args, **kwargs):
            run_date_time = datetime.now()
            function_name = function.__name__
            result = function(*args, **kwargs)
            with open('log_some_func.txt', 'a', encoding='utf-8') as file:
                file.write(f'Function run Date-Time: {run_date_time}\n'
                           f'Function name: {function_name}\n'
                           f'Function arguments: {args, kwargs}\n'
                           f'Function execution result: {result}\n'
                           '-------------------------------------\n')
            return result
        return new_function
    return decor


@get_log
def rectangle_area(length, width):
    area = length * width
    return area


@get_log_1(parameter=log_file_path)
def rectangle_perimeter(length, width):
    perimeter = (length + width) * 2
    return perimeter


if __name__ == '__main__':
    print('Let\'s count rectangle perimeter or area. \nCommands available: p - perimeter, a - area, q - quit')
    while True:
        command = input('Enter a command: ')

        if command == 'a':
            print(
                f"Rectangle area is: {rectangle_area(int(input('Enter rectangle length: ')), (int(input('Enter rectangle width: '))))}")
        elif command == 'p':
            print(
                f"Rectangle perimeter is: {rectangle_perimeter(int(input('Enter rectangle length: ')), (int(input('Enter rectangle width: '))))}")
        elif command == 'q':
            print('Good bye!')
            break
        else:
            print('invalid command!')
