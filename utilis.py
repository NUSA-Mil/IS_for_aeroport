def safe_input(prompt, validation_func, error_message="Неверный ввод. Попробуйте снова."):
    while True:
        value = input(prompt)
        if validation_func(value):
            return value
        else:
            print(error_message)
