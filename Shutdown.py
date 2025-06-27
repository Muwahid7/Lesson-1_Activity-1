def shutdown():
    Answer = input("Do you want to shut down the computer?(yes/no)")
    if Answer == "yes":
        print("Shutting down the system")
    elif Answer == "no":
        print("Shutdown cancelled.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

shutdown()