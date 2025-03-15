from tkinter import *
import speedtest
import threading

def get_speed():
    def run_speed_test():
        st = speedtest.Speedtest()
        download = st.download()
        upload = st.upload()
        download_speed = round(download / (10**6), 2)
        upload_speed = round(upload / (10**6), 2)
        download_label.config(text=f"{download_speed} Mbps")
        upload_label.config(text=f"{upload_speed} Mbps")

    threading.Thread(target=run_speed_test).start()

SP = Tk()
SP.title("Speed Test")
SP.geometry("500x500")
SP.configure(bg="black")

btn = Button(SP, text="Get Speed", font=("Arial", 20), bg="black", fg="white", command=get_speed)
btn.place(x=60, y=420, height=50, width=380)

Label(SP, text="Speed Test", font=("Arial", 20), bg="black", fg="white").place(x=60, y=40, height=50, width=380)
Label(SP, text="Download Speed", font=("Arial", 20), bg="black", fg="white").place(x=60, y=130, height=50, width=380)
download_label = Label(SP, text="00", font=("Arial", 20), bg="black", fg="white")
download_label.place(x=60, y=200, height=50, width=380)
Label(SP, text="Upload Speed", font=("Arial", 20), bg="black", fg="white").place(x=60, y=290, height=50, width=380)
upload_label = Label(SP, text="00", font=("Arial", 20), bg="black", fg="white")
upload_label.place(x=60, y=360, height=50, width=380)

SP.mainloop()