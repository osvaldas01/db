from regex_assignments.regex_assignments import *

if __name__ == '__main__':
    program = RegProgram("12.12.2020")
    # print(program.change_date())
    # print(program.print_date())
    # print(program.event_date())
    print(program.censorship("kvaraba", "žaltys"))

    program_2 = RequestProgram()
    # print(program_2.get_html())
    print(program_2.get_links())