############################################# IMPORTING ################################################
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mess
import tkinter.simpledialog as tsd
import cv2, os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time


############################################# FUNCTIONS ################################################

def TakeImages():
    vid = cv2.VideoCapture(0)

    while (True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

def TrackImages():
    vid = cv2.VideoCapture(0)

    while (True):

        # Capture the video frame
        # by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


    ######################################## USED STUFFS ############################################

global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day, month, year = date.split("-")

mont = {'01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
        }

######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True, False)
window.title("He thong diem danh khuon mat")
window.configure(background='#f9f6f2')

frame1 = tk.Frame(window, bg="#e2e2e2")
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80)

frame2 = tk.Frame(window, bg="#e2e2e2")
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Ứng dụng điểm danh khuôn mặt", fg="black", bg="#f9f6f2",
                    width=55, height=1, font=('comic', 29, ' bold '))
message3.place(x=10, y=10)

frame3 = tk.Frame(window, bg="#c4c6ce")
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce")
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text=day + "-" + mont[month] + "-" + year + "  |  ", fg="#f9f6f2", bg="#f9f6f2", width=55,
                 height=1, font=('comic', 22, ' bold '))
datef.pack(fill='both', expand=1)

clock = tk.Label(frame3, fg="black", bg="#f9f6f2", width=55, height=1, font=('comic', 22, ' bold '))
clock.pack(fill='both', expand=1)

head2 = tk.Label(frame2, text="                            Đăng kí mới                              ", fg="black",
                 bg="#d1d1d1", font=('comic', 17, ' bold '))
head2.grid(row=0, column=0)

head1 = tk.Label(frame1, text="                                Đã đăng kí                               ", fg="black",
                 bg="#d1d1d1", font=('comic', 17, ' bold '))
head1.place(x=0, y=0)

lbl = tk.Label(frame2, text="Nhập MSSV:", width=20, height=1, fg="black", bg="#e2e2e2", font=('comic', 17, ' bold '))
lbl.place(x=80, y=55)

txt = tk.Entry(frame2, width=32, fg="black", font=('comic', 15, ' bold '))
txt.place(x=30, y=88)

lbl2 = tk.Label(frame2, text="Nhập họ tên:", width=20, fg="black", bg="#e2e2e2", font=('comic', 17, ' bold '))
lbl2.place(x=80, y=140)

txt2 = tk.Entry(frame2, width=32, fg="black", font=('comic', 15, ' bold '))
txt2.place(x=30, y=173)

message1 = tk.Label(frame2, text="1)Chụp hình  >>>  2)Lưu thông tin", fg="black", bg="#e2e2e2", width=39, height=1,
                    activebackground="#e2e2e2", font=('comic', 15, ' bold '))
message1.place(x=7, y=230)

message = tk.Label(frame2, text="", bg="#e2e2e2", fg="black", width=39, height=1, activebackground="#e2e2e2",
                   font=('comic', 16, ' bold '))
message.place(x=7, y=450)

lbl3 = tk.Label(frame1, text="Bảng điểm danh", width=20, fg="black", bg="#e2e2e2", height=1, font=('comic', 17, ' bold '))
lbl3.place(x=100, y=115)

res = 0
exists = os.path.isfile("StudentDetails/StudentDetails.csv")
if exists:
    with open("StudentDetails/StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1
    csvFile1.close()
else:
    res = 0
message.configure(text='Tổng lượt đăng kí  : ' + str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window, relief='ridge')
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='Đổi mật khẩu')
filemenu.add_command(label='Thoát', command=window.destroy)
menubar.add_cascade(label='Trợ giúp', font=('comic', 29, ' bold '), menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

tv = ttk.Treeview(frame1, height=13, columns=('name', 'date', 'time'))
tv.column('#0', width=82)
tv.column('name', width=130)
tv.column('date', width=133)
tv.column('time', width=133)
tv.grid(row=2, column=0, padx=(0, 0), pady=(150, 0), columnspan=4)
tv.heading('#0', text='ID')
tv.heading('name', text='NAME')
tv.heading('date', text='DATE')
tv.heading('time', text='TIME')

###################### SCROLLBAR ################################

scroll = ttk.Scrollbar(frame1, orient='vertical', command=tv.yview)
scroll.grid(row=2, column=4, padx=(0, 100), pady=(150, 0), sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Xóa", fg="black", bg="#f09ea7", width=11,
                        activebackground="white", font=('comic', 11, ' bold '))
clearButton.place(x=335, y=86)
clearButton2 = tk.Button(frame2, text="Xóa", fg="black", bg="#f09ea7", width=11,
                         activebackground="white", font=('comic', 11, ' bold '))
clearButton2.place(x=335, y=172)
takeImg = tk.Button(frame2, text="Chụp hình", command=TakeImages, fg="black", bg="#e1dbd6", width=34, height=1,
                    activebackground="white", font=('comic', 15, ' bold '))
takeImg.place(x=30, y=300)
trainImg = tk.Button(frame2, text="Lưu thông tin", fg="black", bg="#e1dbd6", width=34, height=1,
                     activebackground="white", font=('comic', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Điểm danh", command=TrackImages, fg="black", bg="#c1ebc0", width=35, height=1,
                     activebackground="white", font=('comic', 15, ' bold '))
trackImg.place(x=30, y=50)
quitWindow = tk.Button(frame1, text="Thoát", command=window.destroy, fg="black", bg="#f09ea7", width=35, height=1,
                       activebackground="white", font=('comic', 15, ' bold '))
quitWindow.place(x=30, y=450)

##################### END ######################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################
