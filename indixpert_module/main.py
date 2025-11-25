
import menu
import registration
import searching
import deleating
import records


def all_operation():
    student_list=[]

    while 1:
        user_menu_choise=menu.user_menu()
        if user_menu_choise==4:
            break
        elif user_menu_choise==1:
            registration.student_registration(student_list)
        elif user_menu_choise==2:
            searching.user_searching(student_list)
        elif user_menu_choise==3:
            deleating.user_deleting(student_list)
        elif user_menu_choise==5:
            records.user_records(student_list)
        else:
            print("WRONG INPUT ! , please try again")


all_operation()