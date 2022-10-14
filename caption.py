import csv

def writing_csv(information_list):
    with open("Student_information.csv",'a',newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact No", "Email Id", "Fee paid", "Remaining fee"])
        writer.writerow(information_list)



if _name_ == '_main_':

    condition = True
    student_num = 1
    Total_fee = 49500

    while(condition):
        student_info = input((f"Enter the student #{student_num} information based on the given format (Name Age Contact_No Email_Id Fee_paid): "))


        student_lst = student_info.split(' ')
        print("The entered split up info is; "+ str(student_lst))
        rem_amount = Total_fee - int(student_lst[4])
        student_lst.append(rem_amount)
     


        check_correctness = input("Is the entered information right?(yes/no):  ")
        if check_correctness == "yes":
            writing_csv(student_lst)
            next_student = input("Do you want to enter the information of the next student?(yes/no): ")
            if next_student == "yes":
                condition = True
                student_num = student_num+1
            elif next_student == "no":
                condition = False
        elif check_correctness == "no":
            print("Please re-enter the values.")
