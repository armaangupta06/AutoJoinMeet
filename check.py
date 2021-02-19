import datetime
from send_messages import send_Message
from execute import join_classes
import time
def loop():

    counter = 0
    period = "B"
    now = datetime.datetime.now()
    current_time = now.strftime("%A")
    # %A is to get the name of the Day!
    justtime = now.strftime("%H:%M")
    print(justtime)
    first_class = "09:46"
    second_class = "10:55"
    third_class = "12:04"
    fourth_class = "13:13"
    
    phonenumber1 = "8568736010"
    phonenumber2 = "8568736000"
    phonenumber3 = "8568733066"
    phonenumber4 = "8567019014"

    period_a = "https://meet.google.com/lookup/cddt6frds7"
    period_b = "https://meet.google.com/lookup/d2thqrbuqj"
    period_c = "https://meet.google.com/lookup/cl6emhz2wl"
    period_d = "https://meet.google.com/lookup/ahxkwhy7rw"
    period_e = "https://meet.google.com/lookup/dfsabsphbp"
    period_f = "https://meet.google.com/lookup/h2emr753d2"
    period_g = "https://meet.google.com/lookup/fzztunstco"
    period_h = "https://meet.google.com/lookup/elsj2rrbqq"
    while True:
        if counter == 0:
            if (justtime == "10:48" or justtime == "11:57" or justtime == "13:06" or justtime == "14:15"):
                send_Message("Class is finished...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                counter += 1
                join_classes(quit=True)
            if (justtime == "09:35" or justtime == "10:44" or justtime == "11:53" or justtime == "13:03"):
                send_Message("Class is starting in 10 minutes...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                counter += 1

            if (justtime == first_class or justtime == second_class or justtime == third_class or justtime == fourth_class):
                if period == "B":
                    if ((current_time == "Tuesday") or (current_time == "Thursday")):
                        if ((justtime == first_class)):
                            # World Civ
                            counter += 1


                            join_classes(period_a)


                        elif ((justtime == second_class)):
                            # Health
                            counter += 1

                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_b)

                        elif ((justtime == third_class)):
                            # Functions
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_e)
                        elif ((justtime == fourth_class)):
                            # English
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_f)

                    elif ((current_time == "Monday") or (current_time == "Wednesday") or (current_time == "Friday")):
                        if ((justtime == first_class)):
                            # Spanish
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_c)

                        elif ((justtime == second_class)):
                            # Biology
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_d)

                        elif ((justtime == third_class)):
                            # Phys Ed
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_g, click=True, type="here")
                        elif ((justtime == fourth_class)):
                            # Intro to Comp Programming
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_h, click=True, type="here")

                elif (period == "A"):

                    if ((current_time == "Monday") or (current_time == "Wednesday") or (current_time == "Friday")):
                        if ((justtime == first_class)):
                            # World Civ
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_a)

                        elif ((justtime == second_class)):
                            # Health
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)

                            join_classes(period_b)

                        elif ((justtime == third_class)):
                            # Functions
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_e)
                        elif ((justtime == fourth_class)):
                            # English
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_f)

                    elif ((current_time == "Tuesday") or (current_time == "Thursday")):
                        if ((justtime == first_class)):
                                # Spanish
                            print("working")
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_c)

                        elif ((justtime == second_class)):
                            # Biology
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_d)

                        elif ((justtime == third_class)):
                            # Phys Ed
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_g, click=True, type = "here")
                        elif ((justtime == fourth_class)):
                            # Intro to Computer Programming
                            counter += 1
                            send_Message("Class is starting...", phonenumber1, phonenumber2, phonenumber3, phonenumber4)
                            join_classes(period_h, click=True, type="here")
            else:
                time.sleep(20)
                now = datetime.datetime.now()
                current_time = now.strftime("%A")
                justtime = now.strftime("%H:%M")

                print(justtime)

        else:
            time.sleep(60)
            now = datetime.datetime.now()
            current_time = now.strftime("%A")
            justtime = now.strftime("%H:%M")

            print(justtime)
            counter = 0


