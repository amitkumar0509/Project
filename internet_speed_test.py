import speedtest

st = speedtest.Speedtest()
print("Download Speed:", st.download() / 10**6, "Mbps")
print("Upload Speed:", st.upload() / 10**6, "Mbps")