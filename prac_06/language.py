from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ruby)
    print(python)
    print(visual_basic)

    object_list = (ruby, python, visual_basic)

    print("The dynamically typed languages are: ")

    for i in range(0, len(object_list), 1):
        if object_list[i].is_dynamic():
            print(object_list[i].field)


main()