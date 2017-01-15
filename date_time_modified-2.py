import os
import datetime
import sys

# The below three varibles store the current date and time such that
# date_time contains both the date and time
# date contains only the date
# time contains only the current time
date_time=str(datetime.datetime.now())
def date(): 
    return str(datetime.datetime.now().date())
#date=
def time(): 
    return str(datetime.datetime.now().time())

#A list which stores all the months in a year
months=['January','February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December']

def prompt():
    '''This function takes a user input and depending on the users choice to
    either continue or quit takes the next action. If the user doesnt input
    the correct value then a message is printed asking for the current input'''
    while True:
        choice= input("Enter your choice- 'Yes' or 'Y' to continue or 'q' to exit: ")
        if choice!='Yes' and choice!='Y' and choice!='q':
            print("Invalid choice.\n Please follow the instructions- 'Yes' or 'Y' to continue or 'q' to exit")
            continue
        elif choice=='q':
            print("Exiting now...")
            sys.exit()
        else:
            folder_path_inp=input("Enter the path where you would like to have the folder created: ")
            old_date=date()
            
            dates=old_date.split("-")
            folder_path= folder_path_inp+ "//" + dates[2] + "-" + months[int(dates[1][1])-1] + "-" + dates[0] + "//"
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            print("Your folder has been created!")
            creation(folder_path,old_date,folder_path_inp)
            

def creation(folder_path,old_date,folder_path_inp):
    '''This function handles the creation of the text files once the folder path is obtained.'''
    if os.path.exists(folder_path):
        while True:
            res=input("Do you want to continue?(Y/Q)")
            temp=folder_path
            if res=='Y':
                new_date=date()
                if old_date!=new_date:
                    dates=date()
                    dates=dates.split("-")
                    old_date=new_date
                    folder_path= folder_path_inp+ "//" + dates[2] + "-" + months[int(dates[1][1])-1] + "-" + dates[0] + "//"
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    temp=folder_path
                    
                new_time=time()
                #print(new_time)
                times=new_time.split(":")
                #print(times)
                temp+=old_date + "_" + times[0]+"-"+ times[1]+"-"+ times[2] + ".txt"
                main=open(temp,'w')
                main.write("Created")
                main.close()
                print("Your file with the appropriate date and time stamp has been saved")
                
                    
            elif res=='Q':
                print("Exiting...")
                sys.exit()
            else:
                print("Invalid choice.\n Please follow the instructions- 'Y' to continue or 'Q' to exit")
                continue
                
if __name__=='__main__':
    prompt()
   
