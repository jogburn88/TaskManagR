import Job


def main():

    job_name = input("Please enter a job name. ")
    due_date = input("Please enter the due date. ")
    new_job = Job.Job(job_name, due_date)
    while True:
        user_input = input("Enter 'date' for the date or 'name' for the name.")

        if user_input == 'date':
            print(new_job.dueDate)
        elif user_input == 'name':
            print(new_job.name)
        elif user_input == 'exit':
            break


if __name__ == '__main__':
    main()
