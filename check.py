import datetime
from send_messages import send_Message
from execute import join_classes
import time
def loop():

    counter = 0
    period = "A"
    now = datetime.datetime.now()
    current_time = now.strftime("%A")
    # %A is to get the name of the Day!
    justtime = now.strftime("%H:%M")
    print(justtime)
    print(current_time)
    first_class = "09:45"
    second_class = "11:00"
    third_class = "12:17"
    fourth_class = "13:35"
    
    phonenumber1 = "8568736010"
    phonenumber2 = ""
    phonenumber3 = "8568733066"
    phonenumber4 = "8568736000"

    period_a = "https://meet.google.com/lookup/cddt6frds7"
    period_b = "https://meet.google.com/lookup/d2thqrbuqj"
    period_c = "https://meet.google.com/lookup/cl6emhz2wl"
    period_d = "https://meet.google.com/lookup/ahxkwhy7rw"
    period_e = "https://meet.google.com/lookup/dfsabsphbp"
    period_f = "https://meet.google.com/lookup/h2emr753d2"
    period_g = "https://meet.google.com/lookup/fzztunstco"
    period_h = "https://meet.google.com/lookup/elsj2rrbqq"
    while True:
        if not(str(current_time) == "Saturday" or str(current_time) == "Sunday"):
            if counter == 0:
                if (justtime == "10:48" or justtime == "12:03" or justtime == "13:18" or justtime == "14:30"):
                    send_Message("Class is finished...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)

                    counter += 1
                    join_classes(quit=True)
                    time.sleep(60)
                if (justtime == "09:35" or justtime == "10:50" or justtime == "12:05" or justtime == "13:17"):
                    send_Message("Class is starting in 10 minutes...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                    counter += 1

                    time.sleep(60)

                if (justtime == first_class or justtime == second_class or justtime == third_class or justtime == fourth_class):
                    if period == "B":
                        if ((current_time == "Tuesday") or (current_time == "Thursday")):
                            if ((justtime == first_class)):
                                # World Civ
                                counter += 1

                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_a)


                            elif ((justtime == second_class)):
                                # Health
                                counter += 1

                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_b)

                            elif ((justtime == third_class)):
                                # Functions
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_e)
                            elif ((justtime == fourth_class)):
                                # English
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_f)

                        elif ((current_time == "Monday") or (current_time == "Wednesday") or (current_time == "Friday")):
                            if ((justtime == first_class)):
                                # Spanish
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_c)

                            elif ((justtime == second_class)):
                                # Biology
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_d)

                            elif ((justtime == third_class)):
                                # Phys Ed
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_g, click=True, type="here")
                            elif ((justtime == fourth_class)):
                                # Intro to Comp Programming
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_h, click=True, type="here")

                    elif (period == "A"):

                        if ((current_time == "Monday") or (current_time == "Wednesday") or (current_time == "Friday")):
                            if ((justtime == first_class)):
                                # World Civ
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_a)

                            elif ((justtime == second_class)):
                                # Health
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_b)

                            elif ((justtime == third_class)):
                                # Functions
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_e)
                            elif ((justtime == fourth_class)):
                                # English
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_f)

                        elif ((current_time == "Tuesday") or (current_time == "Thursday")):
                            if ((justtime == first_class)):
                                    # Spanish
                                print("working")
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_c)

                            elif ((justtime == second_class)):
                                # Biology
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_d)

                            elif ((justtime == third_class)):
                                # Phys Ed
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_g, click=True, type = "here")
                            elif ((justtime == fourth_class)):
                                # Intro to Computer Programming
                                counter += 1
                                send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                                time.sleep(60)
                                join_classes(period_h, click=True, type="here")
                else:
                    time.sleep(0.1)
                    now = datetime.datetime.now()
                    current_time = now.strftime("%A")
                    justtime = now.strftime("%H:%M")


            else:
                now = datetime.datetime.now()
                current_time = now.strftime("%A")
                justtime = now.strftime("%H:%M")

                print(justtime)
                counter = 0


        else:
            break

    print("Done loop")