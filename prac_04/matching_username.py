def main():
    user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    input_username = input("Enter user name: ")

    if input_username in user_names:
        print("Access granted!")
    else:
        print("Access denied!")


main()
