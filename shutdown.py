def shutdown_system():
    x=str(input("Are you sure you want to shutdown the system? (yes/no): "))
    if x == "yes":
        print("Shutting down the system")
    elif x == "no":
        print("Shutdown cancelled")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

shutdown_system()